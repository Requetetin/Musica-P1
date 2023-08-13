# Original Song.py
# Diego Alvarez
# Martin Amado
# Alejandra Gudiel
 
from music import *

original = Score("Original Song", 180)

trumpet1 = Part(TRUMPET, 0)
trumpet2 = Part(TRUMPET, 1)
horn = Part(FRENCH_HORN, 2)
trombone = Part(TROMBONE, 3)

# Part 1
# Trumpet 1

trumpet1Phrase = Phrase()

t1p1 = [REST] + [REST] + [REST] + [REST, [B4, B5], [B4, B5], [A4, A5], [D5, D6], [E5, E6]]
t1d1 = [WN]   + [WN]   + [WN]   + [QN  ,  EN      , EN      , QN      , QN      , QN]

trumpet1Phrase.addNoteList(t1p1, t1d1)
trumpet1.addPhrase(trumpet1Phrase)

# Trumpet 2

trumpet2Phrase = Phrase()

t2p1 = [REST] + [REST] + [REST, E5, E5, D5, G5, G5] + [E5] + [E5]
t2d1 = [WN]   + [WN]   + [QN  , EN, EN, EN, EN, QN] + [WN] + [QN]

trumpet2Phrase.addNoteList(t2p1, t2d1)
trumpet2.addPhrase(trumpet2Phrase)

# Horn

hornPhrase = Phrase()

hop1 = [REST] + [REST, E5, E5, D5, G5] + [E5] + [E5] + [E5]
hod1 = [WN]   + [QN  , EN, EN, QN, QN] + [WN] + [WN] + [QN]

hornPhrase.addNoteList(hop1, hod1)
horn.addPhrase(hornPhrase)

# Trombone

trombonePhrase = Phrase()

trp1 = [D4, D4, D4, C4, F4, F4] + [D4] + [D4] + [D4] + [D4]
trd1 = [QN, EN, EN, EN, EN, QN] + [WN] + [WN] + [WN] + [QN]

trombonePhrase.addNoteList(trp1, trd1)
trombone.addPhrase(trombonePhrase)

### DRUM BEAT
drumsPart = Part("Drums", 0, 9)
drumsPart.setTempo(120.0)

hiHatPhrase = Phrase(12.0)
snarePhrase = Phrase(12.0)
tomPhrase = Phrase(12.0)
kickPhrase = Phrase(12.0)
clapPhrase = Phrase(24.0)
drumsDuration = [SN] * 16

## hiHat
hhtp = [CHH, REST] * 6 + [REST] * 4
hiHatPhrase.addNoteList(hhtp, drumsDuration)

## snare
snrp = [REST] * 4 + [STK, REST, STK, REST] + [REST] * 8
snarePhrase.addNoteList(snrp, drumsDuration)

## tom
tomp = [REST, LFT] + [REST] * 9 + [LFT] * 2 + [REST] * 3 
tomPhrase.addNoteList(tomp, drumsDuration)

## kick
kikp = [BDR] + [REST] * 6 + [BDR] + [REST] * 8
kickPhrase.addNoteList(kikp, drumsDuration)

## Clap
clpp = [REST] * 12 + [CLP, REST] * 2
clapPhrase.addNoteList(clpp, drumsDuration)

## Repeat 6 times, the last 3, add claps
Mod.repeat(hiHatPhrase, 6)
Mod.repeat(snarePhrase, 6)
Mod.repeat(tomPhrase, 6)
Mod.repeat(kickPhrase, 6)
Mod.repeat(clapPhrase, 3)

## Combining drums
drumsPart.addPhrase(hiHatPhrase)
drumsPart.addPhrase(snarePhrase)
drumsPart.addPhrase(tomPhrase)
drumsPart.addPhrase(kickPhrase)
drumsPart.addPhrase(clapPhrase)


## Composing full song

original.addPart(trumpet1)
original.addPart(trumpet2)
original.addPart(horn)
original.addPart(trombone)
original.addPart(drumsPart)
 
#View.sketch(original)
Play.midi(original)
Write.midi(original, "Trial.mid")