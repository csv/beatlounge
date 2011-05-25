# Arpegiattors

from pprint import pformat
import random

from zope.interface import Interface, Attribute, implements

from twisted.python import log

from bl.debug import debug, DEBUG
from bl.utils import getClock


__all__ = [
    'IArp', 'IndexedArp', 'AscArp', 'DescArp', 'OrderedArp', 'RevOrderedArp',
    'RandomArp', 'ArpSwitcher', 'OctaveArp', 'Adder', 'PhraseRecordingArp',
]


class IArp(Interface):
    """
    An interface for arpeggiators.
    """

    values =  Attribute("Values to arpeggiate")

    def reset(values):
        """
        Reset `values` to the given list.
        """

    def __call__():
        """
        Get the next value in the arpeggiation.
        """


class BaseArp(object):
    implements(IArp)

    values = ()

    def __init__(self, values=()):
        self.reset(values)


    def reset(self, values):
        self.values = values


    def __call__(self):
        raise NotImplentedError


def sortNumeric(values, sort=None):
    if sort is None:
        sort = lambda l : list(sorted(l))
    numbers = [ v for v in values if type(v) in (int, float, list, tuple) ]
    numbers = sort(numbers)
    newvalues = []
    for v in values:
        if type(v) in (int, float):
            newvalues.append(numbers.pop(0))
        else:
            newvalues.append(v)
    return newvalues


class IndexedArp(BaseArp):
    index = 0
    count = 0
    direction = 1

    def sort(self, values):
        raise NotImplementedError

    def reset(self, values):
        values = self.sort(values)
        self.count = len(values)
        if self.values:
            factor = len(values) / float(len(self.values))
            if factor != 1:
                self.index = int(self.index * factor)
                self.index = self.index % self.count
                if self.index == self.count:
                    self.index -= 1
            elif self.index >= self.count:
                self.index = self.index % self.count
        self.values = values

    def __call__(self):
        if not self.values:
            return
        if self.index >= len(self.values):
            self.reset(self.values)
        v = self.values[self.index]
        self.index += self.direction
        self.index = self.index % self.count
        return exhaustCall(v)

class AscArp(IndexedArp):

    def sort(self, values):
        return sortNumeric(values)

class DescArp(IndexedArp):

    def sort(self, values):
        return sortNumeric(values, lambda l : list(reversed(sorted(l))))

class OrderedArp(IndexedArp):

    def sort(self, values):
        return values


def RevOrderedArp(values=()):
    arp = OrderedArp(values)
    arp.direction = -1
    arp.index = len(values) - 1
    return arp


def exhaustCall(v):
    while callable(v):
        v = v()
    return v

class RandomArp(BaseArp):

    def reset(self, values):
        self._current = list(values)
        self._next = []
        self.count = len(values)
        self.values = values

    def __call__(self):
        if not self._current:
            self._current = self._next
        if not self._current:
            return
        l = len(self._current)
        index = random.randint(0, l-1)
        next = self._current.pop(index)
        self._next.append(next)
        return next

class ArpSwitcher(BaseArp):

    def __init__(self, arp, values=None):
        if values is None:
            values = arp.values
        self.arp = arp
        self.arp.reset(values)
        self.values = values
        self.count = len(self.values)

    def reset(self, values):
        self.values = values
        self.arp.reset(values)
        self.count = len(values)

    def switch(self, arp):
        arp.reset(self.values)
        self.arp = arp

    def __call__(self):
        return self.arp()



class OctaveArp(ArpSwitcher):

    def __init__(self, arp, values=None, octaves=3, direction=1, oscillate=False):
        ArpSwitcher.__init__(self, arp, values)
        self.octaves = octaves
        self.currentOctave = 0
        self.index = 0
        if direction == -1:
            self.currentOctave = octaves
        self.direction = direction
        self.oscillate = oscillate


    def __call__(self):
        if not self.count:
            return
        v = exhaustCall(self.arp())
        if v is not None:
            v += (self.currentOctave * 12)
        self.index += 1
        self.index = self.index % self.count
        if self.index == 0:
            self.currentOctave += self.direction
            if self.octaves:
                self.currentOctave = self.currentOctave % (self.octaves + 1)
                if self.oscillate and self.currentOctave in (0, self.octaves):
                    self.direction *= -1
            else:
                self.currentOctave = 0
        return v



class PhraseRecordingArp(BaseArp):

    def __init__(self, clock=None):
        self.clock = getClock(clock)
        self._phraseStartTicks = self.clock.ticks
        self._last_tape = None
        self._tape = {}
        self._eraseTape()
        self.phrase = []

    def __call__(self):
        self.elapsed = self._phraseStartTicks = self.clock.ticks
        self._resetRecording()
        return list(self.phrase)

    def _resetRecording(self):
        whens = self._tape['whens']
        notes = self._tape['notes']
        velocities = self._tape['velocities']
        sustains = self._tape['sustains']
        indexes = self._tape['indexes']
        if DEBUG:
            log.msg('>tape===\n%s' % pformat(self._tape))
        self._eraseTape()
        if not whens and (self._last_tape and self._last_tape['dirty']):
            whens = self._last_tape['whens']
            notes = self._last_tape['notes']
            velocities = self._last_tape['velocities']
            sustains = self._last_tape['sustains']
            indexes = self._last_tape['indexes']
            self._last_tape['dirty'] = True
        if whens:
            sus = [None] * len(whens)
            for (ontick, onnote, sustain) in sustains:
                index = indexes.get((ontick, onnote))
                if index is not None:
                    sus[index] = sustain
                else:
                    log.err(ValueError(
                        'no index for tick=%s note=%s' % (ontick, onnote)))
            self.phrase = zip(whens, notes, velocities, sus)
            self.phrase = [ (w,n,v,s or self.elapsed - w) for (w,n,v,s) in self.phrase ]
            if DEBUG:
                log.msg('>phrase===\n%s' % pformat(self.phrase))

    def _eraseTape(self):
        if self._tape and self._tape['whens']:
            self._last_tape = dict(self._tape)
            self._last_tape['dirty'] = False
        self._tape = {'whens':[], 'notes':[], 'velocities':[],
                      'sustains':[], 'indexes':{}, 'last_ticks': {}}


    def recordNoteOn(self, note, velocity=100, ticks=None):
        if ticks is None:
            ticks = self.clock.ticks
        self._tape['indexes'][(self.clock.ticks, note)] = len(self._tape['notes'])
        self._tape['last_ticks'][note] = self.clock.ticks
        self._tape['notes'].append(note)
        self._tape['velocities'].append(velocity)
        self._tape['whens'].append(ticks - self._phraseStartTicks)


    def recordNoteOff(self, note):
        tape = self._tape
        last = tape['last_ticks'].get(note, None)
        if last is None:
            if self._last_tape:
                last = self._last_tape['last_ticks'].get(note, None)
                debug('got last tick from past recording: %s' % last)
                if last is None:
                    log.err(ValueError(
                            'woops, i have not seen noteon event in current '
                            'or last phrase for note: %s' % note))
                    return
            tape = self._last_tape
            tape['dirty'] = True
        sustain = self.clock.ticks - last
        tape['sustains'].append((last, note, sustain))



class Adder(ArpSwitcher):
    """
    A simple wrapper over an Arp instance which will add `amount` to the
    value returned by the wrapped `arp`. The configured `amount`
    can be changed on the fly while the arp is being called.
    """

    def __init__(self, arp, values=None):
        ArpSwitcher.__init__(self, arp, values)
        self.amount = 0

    def __call__(self):
        v = exhaustCall(self.arp())
        if v is not None:
            return self.amount + v


