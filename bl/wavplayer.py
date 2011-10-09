import time
import wave

from warnings import warn
try:
    import pyaudio
except ImportError:
    warn('(bl.wavplayer) requirement pyaudio not available - try installing')
    pyaudio = None

from zope.interface import Interface, Attribute, implements

from twisted.python import log
from twisted.internet.task import coiterate
from twisted.internet.interfaces import IConsumer, IPushProducer

from bl.debug import DEBUG


DEFAULT_CHUNK_SIZE = 4096 / 2


__all__ = ['PyAudioManager', 'WavPlayer', 'IAudioStream', 'IAudioSource',
           'WavFileReader', 'AudioStream']


class PyAudioManager:

    pyaudio = None

    @classmethod
    def init(cls):
        """
        An idempodent init for pyaudio runtime.
        """
        if cls.pyaudio is None:
            cls.pyaudio = pyaudio.PyAudio()
        return cls.pyaudio


class IAudioStream(IConsumer):

    def availableWrite():
        """
        Get number of bytes available to write in stream's buffer.
        """


class IAudioSource(IPushProducer):

    def beingStreaming(stream):
        """
        Begin streaming bytes of audio to a stream (IAudioStream).
        This returns a called which will fire when streaming pauses
        or stops.
        """


class ISeekableAudioSource(Interface):

    def seek(offset):
        """
        Seek to indexed sample (offset) in the audio source.
        """


class IPlayer(Interface):

    source = Attribute("An IAudioSource provider")
    stream = Attribute("An IAudioStream provider")

    def play():
        """
        Begin playing audio - call beginStreaming() on source.
        """

    def pause():
        """
        Pause - call pauseProducing() on source.
        """

    def resume():
        """
        Resume - call resumeProducing() on source.
        """

    def stop():
        """
        Pause playing and finalize source and stream. play() should
        not be called after stop() - use pause() and resume() to
        temporarily stop and then resume playback.
        """

class WavPlayer:
    implements(IPlayer)

    def __init__(self, stream, source):
        """
        stream: L{IAudioStream}
        source: L{IAudioSource}
        """
        self.stream = stream
        self.source = source

    @classmethod
    def fromPath(cls, path, chunkSize=DEFAULT_CHUNK_SIZE, loop=False):
        """
        Convenience method to create an WavPlayer from a filesystem path.
        This creates a news player with an AudioStream and WavFileReader.
        """
        wf = wave.open(path, 'rb')
        p = PyAudioManager.init()
        s = p.open(
                format = p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)
        stream = AudioStream(s)
        source = WavFileReader(wf, chunkSize=chunkSize, loop=loop)
        return cls(stream, source)

    def play(self):
        return self.source.beginStreaming(self.stream)

    def pause(self):
        self.source.pauseProducing()

    def resume(self):
        return self.source.resumeProducing()

    def stop(self):
        self.source.stopProducing()



class AudioStream:
    implements(IAudioStream)

    _source = None

    def __init__(self, stream):
        """
        stream: a pyuadio stream instance
        """
        self.stream = stream

    def registerProducer(self, source, streaming):
        self._source = source

    def unregisterProducer(self):
        self._source = None
        self.stream.close()

    def write(self, data):
        self.stream.write(data)

    def availableWrite(self):
        return self.stream.get_write_available()


class WavFileReader:
    implements(IAudioSource, ISeekableAudioSource)

    stream = None
    _streaming = False

    def __init__(self, wavfile, chunkSize=DEFAULT_CHUNK_SIZE, loop=False):
        self.wavfile = wavfile
        self.chunkSize = chunkSize
        self.loop = loop

    def beginStreaming(self, stream):
        self.stream = stream
        self.stream.registerProducer(self, True)
        self._streaming = True
        return coiterate(self._stream())

    def _stream(self):
        while self._streaming:
            data = self.wavfile.readframes(self.chunkSize)
            while data and self._streaming:
                avl = self.stream.availableWrite()
                if DEBUG:
                    log.msg('write available: %s' % avl)
                if avl >= self.chunkSize:
                    self.stream.write(data)
                    data = self.wavfile.readframes(self.chunkSize)
                    yield data
            if self.loop and self._streaming:
                self.wavfile.setpos(0)
            else:
                break
        self._streaming = False

    def pauseProducing(self):
        self._streaming = False

    def resumeProducing(self):
        self._streaming = True
        return coiterate(self._stream())

    def stopProducing(self):
        self.pauseProducing()
        self.wavfile.close()
        self.stream.unregisterProducer()

    def seek(self, offset):
        self.wavfile.setpos(offset)
