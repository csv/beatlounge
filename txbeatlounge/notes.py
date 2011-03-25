from decimal import Decimal
##############
# Midi notes #
##############

C = [0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
Df = Cs = [1, 13, 25, 37, 49, 61, 73, 85, 97, 109, 121]
D = [2, 14, 26, 38, 50, 62, 74, 86, 98, 110, 122]
Ef = Ds = [3, 15, 27, 39, 51, 63, 75, 87, 99, 111, 123]
E = [4, 16, 28, 40, 52, 64, 76, 88, 100, 112, 124]
F = [5, 17, 29, 41, 53, 65, 77, 89, 101, 113, 125]
Gf = Fs = [6, 18, 30, 42, 54, 66, 78, 90, 102, 114, 126]
G = [7, 19, 31, 43, 55, 67, 79, 91, 103, 115, 127]
Af = Gs = [8, 20, 32, 44, 56, 68, 80, 92, 104, 116]
A = [9, 21, 33, 45, 57, 69, 81, 93, 105, 117]
Bf = As = [10, 22, 34, 46, 58, 70, 82, 94, 106, 118]
B = [11, 23, 35, 47, 59, 71, 83, 95, 107, 119]
MIDI_NOTES = [C, Df, D, Ef, E, F, Gf, G, Af, A, Bf, B]

keys = {'C':0, 'Df':1, 'Cs':1, 'D':2, 'Ds':3, 'Ef':3,
        'E':4, 'F':5, 'Fs':6, 'Gf':6, 'G':7, 'Gs':8,
        'Af':8, 'A':9, 'As':10, 'Bf':10, 'B':11}

def notesStringsForList(li):
    """
    Pass in a list and get out the str() letters that are in there.
    """

    retD = {}
    for note in li:
        if note in C:
            retD['C'] = True
        elif note in Df:
            retD['Df'] = True
        elif note in D:
            retD['D'] = True
        elif note in Ef:
            retD['Ef'] = True
        elif note in E:
            retD['E'] = True
        elif note in F:
            retD['F'] = True
        elif note in Gf:
            retD['Gf'] = True
        elif note in G:
            retD['G'] = True
        elif note in Af:
            retD['Af'] = True
        elif note in A:
            retD['A'] = True
        elif note in Bf:
            retD['Bf'] = True
        elif note in B:
            retD['B'] = True

    return set(retD.keys())

def flattenLists(li):
    """
    Takes a list of lists and returns a flat list of the submembers
    """
    ret = []
    for l in li:
        ret.extend(l)
    return ret



##########
# Chords #
##########

# Triads

# Major
Cmaj = [ [C[i], E[i], G[i]] for i in range(len(C)-1) ]
# Minor
Cmin = [ [C[i], Ef[i], G[i]] for i in range(len(C)-1) ]
# Augmented
Caug = [ [C[i], E[i], Gs[i]] for i in range(len(C)-1) ]
# Diminished
Cdim = [ [C[i], Ef[i], Gf[i]] for i in range(len(C)-1) ]

# Seventh Chords

# Diminished seventh
Cdim7 = [ [C[i], Ef[i], Gf[i], A[i]] for i in range(len(C)-1) ]
# Half-diminished seventh
Cm7f5 = [ [C[i], Ef[i], Gf[i], Bf[i]] for i in range(len(C)-1) ]
# Minor seventh
Cmin7 = [ [C[i], Ef[i], G[i], Bf[i]] for i in range(len(C)-1) ]
# Minor major seventh
CmM7 = [ [C[i], Ef[i], G[i], B[i]] for i in range(len(C)-1) ]
# Dominant seventh
Cdom7 = [ [C[i], E[i], G[i], Bf[i]] for i in range(len(C)-1) ]
# Major seventh
Cmaj7 = [ [C[i], E[i], G[i], B[i]] for i in range(len(C)-1) ]
# Augmented seventh
Caug7 = [ [C[i], E[i], Gs[i], Bf[i]] for i in range(len(C)-1) ]
# Augmented major seventh
CM7s5 = [ [C[i], E[i], Gs[i], B[i]] for i in range(len(C)-1) ]


# Extended Chords

# Dominant 9th
C9 = [ [C[i], E[i], G[i], Bf[i], D[i+1]] for i in range(len(C)-2)]
# Dominant 11th
C11 = [ [C[i], E[i], G[i], Bf[i], D[i+1], F[i+1]] for i in range(len(C)-2)]
# Dominant 13th
C13 = [ [C[i], E[i], G[i], Bf[i], D[i+1], F[i+1], A[i+1]] for i in range(len(C)-2)]
# Major 9th
Cmaj9 = [ [C[i], E[i], G[i], B[i], D[i+1]] for i in range(len(C)-2)]
# Major 11th
Cmaj11 = [ [C[i], E[i], G[i], B[i], D[i+1], F[i+1]] for i in range(len(C)-2)]
# Major 13th
Cmaj13 = [ [C[i], E[i], G[i], B[i], D[i+1], F[i+1], A[i+1]] for i in range(len(C)-2)]
# Minor 9th
Cmin9 = [ [C[i], Ef[i], G[i], Bf[i], D[i+1]] for i in range(len(C)-2)]
# Minor 11th
Cmin11 = [ [C[i], Ef[i], G[i], Bf[i], D[i+1], F[i+1]] for i in range(len(C)-2)]
# Minor 13th
Cmin13 = [ [C[i], Ef[i], G[i], Bf[i], D[i+1], F[i+1], A[i+1]] for i in range(len(C)-2)]


# Suspended chords

Csus4 = [ [C[i], F[i], G[i]] for i in range(len(C)-1) ]
Csus2 = [ [C[i], D[i], G[i]] for i in range(len(C)-1) ]

_raise = lambda l,i : [ [e+i for e in k] for k in l]

Csmaj = Dfmaj = _raise(Cmaj, 1)
Dmaj = _raise(Cmaj, 2)
Dsmaj = Efmaj = _raise(Cmaj, 3)
Emaj = _raise(Cmaj, 4)
Fmaj = _raise(Cmaj, 5)
Fsmaj = Gfmaj =  _raise(Cmaj, 6)
Gmaj = _raise(Cmaj, 7)
Gsmaj = Afmaj = _raise(Cmaj, 8)
Amaj = _raise(Cmaj, 9)
Asmaj = Bfmaj = _raise(Cmaj, 10)
Bmaj = _raise(Cmaj, 11)

Csmin = Dfmin = _raise(Cmin, 1)
Dmin = _raise(Cmin, 2)
Dsmin = Efmin = _raise(Cmin, 3)
Emin = _raise(Cmin, 4)
Fmin = _raise(Cmin, 5)
Fsmin = Gfmin =  _raise(Cmin, 6)
Gmin = _raise(Cmin, 7)
Gsmin = Afmin = _raise(Cmin, 8)
Amin = _raise(Cmin, 9)
Asmin = Bfmin = _raise(Cmin, 10)
Bmin = _raise(Cmin, 11)

Csaug = Dfaug = _raise(Caug, 1)
Daug = _raise(Caug, 2)
Dsaug = Efaug = _raise(Caug, 3)
Eaug = _raise(Caug, 4)
Faug = _raise(Caug, 5)
Fsaug = Gfaug =  _raise(Caug, 6)
Gaug = _raise(Caug, 7)
Gsaug = Afaug = _raise(Caug, 8)
Aaug = _raise(Caug, 9)
Asaug = Bfaug = _raise(Caug, 10)
Baug = _raise(Caug, 11)

Csdim = Dfdim = _raise(Cdim, 1)
Ddim = _raise(Cdim, 2)
Dsdim = Efdim = _raise(Cdim, 3)
Edim = _raise(Cdim, 4)
Fdim = _raise(Cdim, 5)
Fsdim = Gfdim =  _raise(Cdim, 6)
Gdim = _raise(Cdim, 7)
Gsdim = Afdim = _raise(Cdim, 8)
Adim = _raise(Cdim, 9)
Asdim = Bfdim = _raise(Cdim, 10)
Bdim = _raise(Cdim, 11)

Csdim7 = Dfdim7 = _raise(Cdim7, 1)
Ddim7 = _raise(Cdim7, 2)
Dsdim7 = Efdim7 = _raise(Cdim7, 3)
Edim7 = _raise(Cdim7, 4)
Fdim7 = _raise(Cdim7, 5)
Fsdim7 = Gfdim7 =  _raise(Cdim7, 6)
Gdim7 = _raise(Cdim7, 7)
Gsdim7 = Afdim7 = _raise(Cdim7, 8)
Adim7 = _raise(Cdim7, 9)
Asdim7 = Bfdim7 = _raise(Cdim7, 10)
Bdim7 = _raise(Cdim7, 11)

Csm7f5 = Dfm7f5 = _raise(Cm7f5, 1)
Dm7f5 = _raise(Cm7f5, 2)
Dsm7f5 = Efm7f5 = _raise(Cm7f5, 3)
Em7f5 = _raise(Cm7f5, 4)
Fm7f5 = _raise(Cm7f5, 5)
Fsm7f5 = Gfm7f5 =  _raise(Cm7f5, 6)
Gm7f5 = _raise(Cm7f5, 7)
Gsm7f5 = Afm7f5 = _raise(Cm7f5, 8)
Am7f5 = _raise(Cm7f5, 9)
Asm7f5 = Bfm7f5 = _raise(Cm7f5, 10)
Bm7f5 = _raise(Cm7f5, 11)

Csmin7 = Dfmin7 = _raise(Cmin7, 1)
Dmin7 = _raise(Cmin7, 2)
Dsmin7 = Efmin7 = _raise(Cmin7, 3)
Emin7 = _raise(Cmin7, 4)
Fmin7 = _raise(Cmin7, 5)
Fsmin7 = Gfmin7 =  _raise(Cmin7, 6)
Gmin7 = _raise(Cmin7, 7)
Gsmin7 = Afmin7 = _raise(Cmin7, 8)
Amin7 = _raise(Cmin7, 9)
Asmin7 = Bfmin7 = _raise(Cmin7, 10)
Bmin7 = _raise(Cmin7, 11)

CsmM7 = DfmM7 = _raise(CmM7, 1)
DmM7 = _raise(CmM7, 2)
DsmM7 = EfmM7 = _raise(CmM7, 3)
EmM7 = _raise(CmM7, 4)
FmM7 = _raise(CmM7, 5)
FsmM7 = GfmM7 =  _raise(CmM7, 6)
GmM7 = _raise(CmM7, 7)
GsmM7 = AfmM7 = _raise(CmM7, 8)
AmM7 = _raise(CmM7, 9)
AsmM7 = BfmM7 = _raise(CmM7, 10)
BmM7 = _raise(CmM7, 11)

Csdom7 = Dfdom7 = _raise(Cdom7, 1)
Ddom7 = _raise(Cdom7, 2)
Dsdom7 = Efdom7 = _raise(Cdom7, 3)
Edom7 = _raise(Cdom7, 4)
Fdom7 = _raise(Cdom7, 5)
Fsdom7 = Gfdom7 =  _raise(Cdom7, 6)
Gdom7 = _raise(Cdom7, 7)
Gsdom7 = Afdom7 = _raise(Cdom7, 8)
Adom7 = _raise(Cdom7, 9)
Asdom7 = Bfdom7 = _raise(Cdom7, 10)
Bdom7 = _raise(Cdom7, 11)

Csmaj7 = Dfmaj7 = _raise(Cmaj7, 1)
Dmaj7 = _raise(Cmaj7, 2)
Dsmaj7 = Efmaj7 = _raise(Cmaj7, 3)
Emaj7 = _raise(Cmaj7, 4)
Fmaj7 = _raise(Cmaj7, 5)
Fsmaj7 = Gfmaj7 =  _raise(Cmaj7, 6)
Gmaj7 = _raise(Cmaj7, 7)
Gsmaj7 = Afmaj7 = _raise(Cmaj7, 8)
Amaj7 = _raise(Cmaj7, 9)
Asmaj7 = Bfmaj7 = _raise(Cmaj7, 10)
Bmaj7 = _raise(Cmaj7, 11)

Csaug7 = Dfaug7 = _raise(Caug7, 1)
Daug7 = _raise(Caug7, 2)
Dsaug7 = Efaug7 = _raise(Caug7, 3)
Eaug7 = _raise(Caug7, 4)
Faug7 = _raise(Caug7, 5)
Fsaug7 = Gfaug7 =  _raise(Caug7, 6)
Gaug7 = _raise(Caug7, 7)
Gsaug7 = Afaug7 = _raise(Caug7, 8)
Aaug7 = _raise(Caug7, 9)
Asaug7 = Bfaug7 = _raise(Caug7, 10)
Baug7 = _raise(Caug7, 11)

CsM7s5 = DfM7s5 = _raise(CM7s5, 1)
DM7s5 = _raise(CM7s5, 2)
DsM7s5 = EfM7s5 = _raise(CM7s5, 3)
EM7s5 = _raise(CM7s5, 4)
FM7s5 = _raise(CM7s5, 5)
FsM7s5 = GfM7s5 =  _raise(CM7s5, 6)
GM7s5 = _raise(CM7s5, 7)
GsM7s5 = AfM7s5 = _raise(CM7s5, 8)
AM7s5 = _raise(CM7s5, 9)
AsM7s5 = BfM7s5 = _raise(CM7s5, 10)
BM7s5 = _raise(CM7s5, 11)

Cs9 = Df9 = _raise(C9, 1)
D9 = _raise(C9, 2)
Ds9 = Ef9 = _raise(C9, 3)
E9 = _raise(C9, 4)
F9 = _raise(C9, 5)
Fs9 = Gf9 =  _raise(C9, 6)
G9 = _raise(C9, 7)
Gs9 = Af9 = _raise(C9, 8)
A9 = _raise(C9, 9)
As9 = Bf9 = _raise(C9, 10)
B9 = _raise(C9, 11)

Csmaj9 = Dfmaj9 = _raise(Cmaj9, 1)
Dmaj9 = _raise(Cmaj9, 2)
Dsmaj9 = Efmaj9 = _raise(Cmaj9, 3)
Emaj9 = _raise(Cmaj9, 4)
Fmaj9 = _raise(Cmaj9, 5)
Fsmaj9 = Gfmaj9 =  _raise(Cmaj9, 6)
Gmaj9 = _raise(Cmaj9, 7)
Gsmaj9 = Afmaj9 = _raise(Cmaj9, 8)
Amaj9 = _raise(Cmaj9, 9)
Asmaj9 = Bfmaj9 = _raise(Cmaj9, 10)
Bmaj9 = _raise(Cmaj9, 11)

Csmin9 = Dfmin9 = _raise(Cmin9, 1)
Dmin9 = _raise(Cmin9, 2)
Dsmin9 = Efmin9 = _raise(Cmin9, 3)
Emin9 = _raise(Cmin9, 4)
Fmin9 = _raise(Cmin9, 5)
Fsmin9 = Gfmin9 =  _raise(Cmin9, 6)
Gmin9 = _raise(Cmin9, 7)
Gsmin9 = Afmin9 = _raise(Cmin9, 8)
Amin9 = _raise(Cmin9, 9)
Asmin9 = Bfmin9 = _raise(Cmin9, 10)
Bmin9 = _raise(Cmin9, 11)

Cs11 = Df11 = _raise(C11, 1)
D11 = _raise(C11, 2)
Ds11 = Ef11 = _raise(C11, 3)
E11 = _raise(C11, 4)
F11 = _raise(C11, 5)
Fs11 = Gf11 =  _raise(C11, 6)
G11 = _raise(C11, 7)
Gs11 = Af11 = _raise(C11, 8)
A11 = _raise(C11, 9)
As11 = Bf11 = _raise(C11, 10)
B11 = _raise(C11, 11)

Csmaj11 = Dfmaj11 = _raise(Cmaj11, 1)
Dmaj11 = _raise(Cmaj11, 2)
Dsmaj11 = Efmaj11 = _raise(Cmaj11, 3)
Emaj11 = _raise(Cmaj11, 4)
Fmaj11 = _raise(Cmaj11, 5)
Fsmaj11 = Gfmaj11 =  _raise(Cmaj11, 6)
Gmaj11 = _raise(Cmaj11, 7)
Gsmaj11 = Afmaj11 = _raise(Cmaj11, 8)
Amaj11 = _raise(Cmaj11, 9)
Asmaj11 = Bfmaj11 = _raise(Cmaj11, 10)
Bmaj11 = _raise(Cmaj11, 11)

Csmin11 = Dfmin11 = _raise(Cmin11, 1)
Dmin11 = _raise(Cmin11, 2)
Dsmin11 = Efmin11 = _raise(Cmin11, 3)
Emin11 = _raise(Cmin11, 4)
Fmin11 = _raise(Cmin11, 5)
Fsmin11 = Gfmin11 =  _raise(Cmin11, 6)
Gmin11 = _raise(Cmin11, 7)
Gsmin11 = Afmin11 = _raise(Cmin11, 8)
Amin11 = _raise(Cmin11, 9)
Asmin11 = Bfmin11 = _raise(Cmin11, 10)
Bmin11 = _raise(Cmin11, 11)

Cs13 = Df13 = _raise(C13, 1)
D13 = _raise(C13, 2)
Ds13 = Ef13 = _raise(C13, 3)
E13 = _raise(C13, 4)
F13 = _raise(C13, 5)
Fs13 = Gf13 =  _raise(C13, 6)
G13 = _raise(C13, 7)
Gs13 = Af13 = _raise(C13, 8)
A13 = _raise(C13, 9)
As13 = Bf13 = _raise(C13, 10)
B13 = _raise(C13, 11)

Csmaj13 = Dfmaj13 = _raise(Cmaj13, 1)
Dmaj13 = _raise(Cmaj13, 2)
Dsmaj13 = Efmaj13 = _raise(Cmaj13, 3)
Emaj13 = _raise(Cmaj13, 4)
Fmaj13 = _raise(Cmaj13, 5)
Fsmaj13 = Gfmaj13 =  _raise(Cmaj13, 6)
Gmaj13 = _raise(Cmaj13, 7)
Gsmaj13 = Afmaj13 = _raise(Cmaj13, 8)
Amaj13 = _raise(Cmaj13, 9)
Asmaj13 = Bfmaj13 = _raise(Cmaj13, 10)
Bmaj13 = _raise(Cmaj13, 11)

Csmin13 = Dfmin13 = _raise(Cmin13, 1)
Dmin13 = _raise(Cmin13, 2)
Dsmin13 = Efmin13 = _raise(Cmin13, 3)
Emin13 = _raise(Cmin13, 4)
Fmin13 = _raise(Cmin13, 5)
Fsmin13 = Gfmin13 =  _raise(Cmin13, 6)
Gmin13 = _raise(Cmin13, 7)
Gsmin13 = Afmin13 = _raise(Cmin13, 8)
Amin13 = _raise(Cmin13, 9)
Asmin13 = Bfmin13 = _raise(Cmin13, 10)
Bmin13 = _raise(Cmin13, 11)

Cssus4 = Dfsus4 = _raise(Csus4, 1)
Dsus4 = _raise(Csus4, 2)
Dssus4 = Efsus4 = _raise(Csus4, 3)
Esus4 = _raise(Csus4, 4)
Fsus4 = _raise(Csus4, 5)
Fssus4 = Gfsus4 =  _raise(Csus4, 6)
Gsus4 = _raise(Csus4, 7)
Gssus4 = Afsus4 = _raise(Csus4, 8)
Asus4 = _raise(Csus4, 9)
Assus4 = Bfsus4 = _raise(Csus4, 10)
Bsus4 = _raise(Csus4, 11)

Cssus2 = Dfsus2 = _raise(Csus2, 1)
Dsus2 = _raise(Csus2, 2)
Dssus2 = Efsus2 = _raise(Csus2, 3)
Esus2 = _raise(Csus2, 4)
Fsus2 = _raise(Csus2, 5)
Fssus2 = Gfsus2 =  _raise(Csus2, 6)
Gsus2 = _raise(Csus2, 7)
Gssus2 = Afsus2 = _raise(Csus2, 8)
Asus2 = _raise(Csus2, 9)
Assus2 = Bfsus2 = _raise(Csus2, 10)
Bsus2 = _raise(Csus2, 11)

chord_choices = [
	A11, A13, A9, AM7s5, Aaug, Aaug7, Adim, Adim7, Adom7, Af11, Af13, Af9, AfM7s5, Afaug, Afaug7,
	Afdim, Afdim7, Afdom7, Afm7f5, AfmM7, Afmaj, Afmaj11, Afmaj13, Afmaj7, Afmaj9, Afmin, Afmin11, Afmin13,
	Afmin7, Afmin9, Afsus2, Afsus4, Am7f5, AmM7, Amaj, Amaj11, Amaj13, Amaj7, Amaj9, Amin, Amin11, Amin13,
	Amin7, Amin9, As11, As13, As9, AsM7s5, Asaug, Asaug7, Asdim, Asdim7, Asdom7, Asm7f5, AsmM7, Asmaj,
	Asmaj11, Asmaj13, Asmaj7, Asmaj9, Asmin, Asmin11, Asmin13, Asmin7, Asmin9, Assus2, Assus4, Asus2, Asus4,
	B11, B13, B9, BM7s5, Baug, Baug7, Bdim, Bdim7, Bdom7, Bf11, Bf13, Bf9, BfM7s5, Bfaug, Bfaug7, Bfdim, Bfdim7,
	Bfdom7, Bfm7f5, BfmM7, Bfmaj, Bfmaj11, Bfmaj13, Bfmaj7, Bfmaj9, Bfmin, Bfmin11, Bfmin13, Bfmin7, Bfmin9,
	Bfsus2, Bfsus4, Bm7f5, BmM7, Bmaj, Bmaj11, Bmaj13, Bmaj7, Bmaj9, Bmin, Bmin11, Bmin13, Bmin7, Bmin9, Bsus2,
	Bsus4, C11, C13, C9, CM7s5, Caug, Caug7, Cdim, Cdim7, Cdom7, Cm7f5, CmM7, Cmaj, Cmaj11, Cmaj13, Cmaj7, Cmaj9,
	Cmin, Cmin11, Cmin13, Cmin7, Cmin9, Cs11, Cs13, Cs9, CsM7s5, Csaug, Csaug7, Csdim, Csdim7, Csdom7, Csm7f5,
	CsmM7, Csmaj, Csmaj11, Csmaj13, Csmaj7, Csmaj9, Csmin, Csmin11, Csmin13, Csmin7, Csmin9, Cssus2, Cssus4,
	Csus2, Csus4, D11, D13, D9, DM7s5, Daug, Daug7, Ddim, Ddim7, Ddom7, Df11, Df13, Df9, DfM7s5, Dfaug,
	Dfaug7, Dfdim, Dfdim7, Dfdom7, Dfm7f5, DfmM7, Dfmaj, Dfmaj11, Dfmaj13, Dfmaj7, Dfmaj9, Dfmin, Dfmin11, Dfmin13,
	Dfmin7, Dfmin9, Dfsus2, Dfsus4, Dm7f5, DmM7, Dmaj, Dmaj11, Dmaj13, Dmaj7, Dmaj9, Dmin, Dmin11, Dmin13, Dmin7,
	Dmin9, Ds11, Ds13, Ds9, DsM7s5, Dsaug, Dsaug7, Dsdim, Dsdim7, Dsdom7, Dsm7f5, DsmM7, Dsmaj, Dsmaj11,
	Dsmaj13, Dsmaj7, Dsmaj9, Dsmin, Dsmin11, Dsmin13, Dsmin7, Dsmin9, Dssus2, Dssus4, Dsus2, Dsus4,
	E11, E13, E9, EM7s5, Eaug, Eaug7, Edim, Edim7, Edom7, Ef11, Ef13, Ef9, EfM7s5, Efaug, Efaug7, Efdim,
	Efdim7, Efdom7, Efm7f5, EfmM7, Efmaj, Efmaj11, Efmaj13, Efmaj7, Efmaj9, Efmin, Efmin11, Efmin13, Efmin7,
	Efmin9, Efsus2, Efsus4, Em7f5, EmM7, Emaj, Emaj11, Emaj13, Emaj7, Emaj9, Emin, Emin11, Emin13, Emin7, Emin9,
	Esus2, Esus4, F11, F13, F9, FM7s5, Faug, Faug7, Fdim, Fdim7, Fdom7, Fm7f5, FmM7, Fmaj, Fmaj11, Fmaj13,
	Fmaj7, Fmaj9, Fmin, Fmin11, Fmin13, Fmin7, Fmin9, Fs11, Fs13, Fs9, FsM7s5, Fsaug, Fsaug7, Fsdim, Fsdim7,
	Fsdom7, Fsm7f5, FsmM7, Fsmaj, Fsmaj11, Fsmaj13, Fsmaj7, Fsmaj9, Fsmin, Fsmin11, Fsmin13, Fsmin7, Fsmin9,
	Fssus2, Fssus4, Fsus2, Fsus4, G11, G13, G9, GM7s5, Gaug, Gaug7, Gdim, Gdim7, Gdom7, Gf11, Gf13, Gf9,
	GfM7s5, Gfaug, Gfaug7, Gfdim, Gfdim7, Gfdom7, Gfm7f5, GfmM7, Gfmaj, Gfmaj11, Gfmaj13, Gfmaj7, Gfmaj9, Gfmin,
	Gfmin11, Gfmin13, Gfmin7, Gfmin9, Gfsus2, Gfsus4, Gm7f5, GmM7, Gmaj, Gmaj11, Gmaj13, Gmaj7, Gmaj9, Gmin,
	Gmin11, Gmin13, Gmin7, Gmin9, Gs11, Gs13, Gs9, GsM7s5, Gsaug, Gsaug7, Gsdim, Gsdim7, Gsdom7, Gsm7f5,
	GsmM7, Gsmaj, Gsmaj11, Gsmaj13, Gsmaj7, Gsmaj9, Gsmin, Gsmin11, Gsmin13, Gsmin7, Gsmin9, Gssus2, Gssus4,
	Gsus2, Gsus4
]




del _raise


_midi = lambda v : (v > 127) and (v - 12) or v

def invert(chord, inversion=1):
    if inversion < 0 or inversion > 4:
        raise ValueError('inversion argument must be one of: 0, 1, 2, 3, 4')
    if not inversion:
        return chord
    first = _midi(chord[0] + 12)
    second = chord[1]
    third = chord[2]
    if inversion >= 2:
        second = _midi(chord[1] + 12)
    if inversion >= 3:
        third = _midi(chord[2] + 12)
    if len(chord) >= 4:
        fourth = chord[3]
        if inversion >= 4:
            fourth = _midi(chord[3] + 12)
    if len(chord) == 3:
        return [ first, second, third ]
    return [ first, second, third, fourth ] + chord[4:]



# Scale definitions and function

def keyScale(scale, key='C', octave=0):
    base = keys[key]
    octave = octave * 12
    return [ n + base + octave for n in scale ]


# pentatonic

majorpenta = pentatonic = [ C[0], D[0], E[0], G[0], A[0],  ]
minorpenta = [ C[0], Ef[0], F[0], G[0], Bf[0],  ] 
egyptpenta = suspenta = [ C[0], D[0], F[0], G[0], Bf[0],  ]
bluesminor = mangong = [ C[0], Ef[0], F[0], Af[0], Bf[0],  ]
bluesmajor = ritusen = [ C[0], D[0], F[0], G[0], A[0],  ] 
insen = [ C[0], Df[0], F[0], G[0], Bf[0],  ]
hirajoshi = hirachoshi = [ C[0], D[0], Ef[0], G[0], Af[0],  ]
iwato = [ C[0], Df[0], F[0], Gf[0], Bf[0],  ]  
kumoi = [ C[0], Df[0], F[0], G[0], Af[0],  ]

# hexatonic

wholetone = [ C[0], D[0], E[0], Fs[0], Gs[0], As[0],  ]
augmented = [ C[0], Ef[0], E[0], G[0], Gs[0], B[0],  ]
prometheus = [ C[0], D[0], E[0], Fs[0], A[0], Bf[0],  ]
blues = [ C[0], Ef[0], F[0], Fs[0], G[0], Bf[0],  ]
tritone = [ C[0], Df[0], E[0], Gf[0], G[0], Bf[0],  ]
tstritone = twoSemitoneTritone = [ C[0], Df[0], D[0], Fs[0], G[0], Bf[0],  ]

# heptatonic

major = ionian = [ C[0], D[0], E[0], F[0], G[0], A[0], B[0],  ]
melodic = melodiciMinor = [ C[0], D[0], Ef[0], F[0], G[0], A[0], B[0],  ]
dorian = [ C[0], D[0], Ef[0], F[0], G[0], A[0], Bf[0],  ]
aeolian = naturalMinor = [ C[0], D[0], Ef[0], F[0], G[0], Af[0], Bf[0],  ]
mixolydian = [ C[0], D[0], E[0], F[0], G[0], A[0], Bf[0],  ]
lydian = [ C[0], D[0], E[0], Fs[0], G[0], A[0], B[0],  ]
byzantine = hungarian = egyptian = [ C[0], D[0], Ef[0], Fs[0], G[0], Af[0], B[0],  ] 
phrygian = [ C[0], Df[0], Ef[0], F[0], G[0], Af[0], Bf[0],  ]
phrygianDominant = [ C[0], Df[0], E[0], F[0], G[0], Af[0], Bf[0],  ]
locrian = [ C[0], Df[0], Ef[0], F[0], Gf[0], Af[0], Bf[0],  ]  
arabic = [ C[0], Df[0], E[0], F[0], G[0], Af[0], B[0],  ]

# ocotatonic

diminished = [ C[0], D[0], Ef[0], F[0], Gf[0], Af[0], A[0], B[0],  ]

def getChordsFromNote(note="C"):
    import txbeatlounge
    chords = []
    for candidate in chord_choices:
        if any([n in flattenLists(candidate) for n in getattr(txbeatlounge.notes, note)]):
            chords.append(candidate)
    return chords

key_strings = ["C", "Df", "D", "Ef", "E", "F", "Gf", "G", "Af", "A", "Bf", "B"]

scale_strings = (
    "majorpenta", "minorpenta", "suspenta", "mangong", "ritusen", "insen", "hirajoshi",
    "iwato", "kumoi", "wholetone", "augmented", "prometheus", "blues", "tritone",
    "tstritone", "major", "melodic", "dorian", "aeolian", "mixolydian", "lydian",
    "byzantine", "phrygian", "phrygianDominant", "locrian", "arabic"
)

def getScalesKeysFromNote(note="C"):
    import txbeatlounge
    scale_keys = []
    for scale_string in scale_strings:
        scale = getattr(txbeatlounge.notes, scale_string)
        for key in key_strings:
            scale = keyScale(scale, key)
            if any([n in scale for n in getattr(txbeatlounge.notes, note)]):
                scale_keys.append((scale_string, key))
    return scale_keys


twelve_tone_equal_440 = [440*(2**(i/Decimal(12))) for i in range(-57,71)]

def freqForNote(note="C"):
    import txbeatlounge
    freqs = []
    for n in getattr(txbeatlounge.notes, note):
        freqs.append(twelve_tone_equal_440[n])
    return freqs

