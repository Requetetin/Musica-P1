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

### INITIAL DRUM BEAT
drumsPart = Part("Drums", 0, 9)
drumsPart.setTempo(120.0)

hiHatPhrase = Phrase(11.0)
snarePhrase = Phrase(11.0)
tomPhrase = Phrase(11.0)
kickPhrase = Phrase(11.0)
clapPhrase = Phrase(22.0)
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

## Accompanying beat for drums
pizzicatoPart = Part(PIZZICATO_STRINGS, 5)
pizzicatoPart.setTempo(60.0)
pizzicatoPhrase = Phrase(5.5)

pizzicatoPitch = [[B1, B2, D3, FS4], [E2, B2, E3, G3]]
pizzicatoDuration = [1.25, 0.75]
pizzicatoPhrase.addNoteList(pizzicatoPitch, pizzicatoDuration)
Mod.repeat(pizzicatoPhrase, 8)
pizzicatoPart.addPhrase(pizzicatoPhrase)


## MAIN DRUM BEAT
mainDrumsPart = Part("Main drum beat", 0, 9)
mainDrumsPart.setTempo(120.0)

mainDrumsPart2 = Part("Main drum beat", 0, 9)
mainDrumsPart2.setTempo(120.0)

mainDrumPhrase = Phrase(35.0)
mainDrumPhrase2 = Phrase(184.0)
mainDrumPitch = [[SNR, BDR], CHH, REST, CHH, SNR, SNR, SNR, CHH, OHH, CHH, SNR, REST, BDR, SNR, CHH, REST]
mainDrumDurat = [SN] * 16
mainDrumPhrase.addNoteList(mainDrumPitch, mainDrumDurat)
mainDrumPhrase2.addNoteList(mainDrumPitch, mainDrumDurat)
Mod.repeat(mainDrumPhrase, 18)
Mod.repeat(mainDrumPhrase2, 12)
mainDrumsPart.addPhrase(mainDrumPhrase)
mainDrumsPart2.addPhrase(mainDrumPhrase2)

## Electric Bass beat
electricBassPart = Part(ELECTRIC_BASS, 4)
electricBassPart.setTempo(120.0)
electricBassPart2 = Part(ELECTRIC_BASS, 4)
electricBassPart2.setTempo(120.0)

electricBassPhrase = Phrase(35.0)
electricBassPhrase2 = Phrase(184.0)
electricBassPitch =    [C3,  REST, C3, B2, B2, B2, REST, REST, REST, B2, E2, E3, D3, REST, D3, D4, D3, A2,  REST, AS2, B2, B2, B2, REST, REST, REST, FS2, E2, REST, G2, A2, B2, C3,  REST, C3, B2, B2, B2, REST, REST, REST, B2, E2, E3, D3, REST, D3, D4, D3, A2,  REST, A2, B2, B2, B2, REST, REST, REST, FS2, E2, REST, G2, A2, B2]
electricBassDuration = [DQN, SN,   SN, SN, EN, SN, SN,   SN,   SN,   SN, QN, QN, QN, SN,   SN, SN, SN, DQN, SN,   SN,  SN, EN, SN, SN,   SN,   SN,   SN,  QN, SN,   SN, SN, SN, DQN, SN,   SN, SN, EN, SN, SN,   SN,   SN,   SN, QN, QN, QN, SN,   SN, SN, SN, DQN, SN,   SN, SN, EN, SN, SN,   SN,   SN,   SN,  QN, SN,   SN, SN, SN]
electricBassPhrase.addNoteList(electricBassPitch, electricBassDuration)
electricBassPhrase2.addNoteList(electricBassPitch, electricBassDuration)
Mod.repeat(electricBassPhrase, 3)
Mod.repeat(electricBassPhrase2, 3)
electricBassPart.addPhrase(electricBassPhrase)
electricBassPart2.addPhrase(electricBassPhrase2)

## Main Trombone beat
mainTromboneBeat = Part(TROMBONE, 3)
mainTromboneBeat.setTempo(120.0)
mainTromboneBeat2 = Part(TROMBONE, 3)
mainTromboneBeat2.setTempo(120.0)

mainTrombonePhrase = Phrase(63.0)
mainTrombonePhrase2 = Phrase(184.0)
## Sample from SpottieOttieDopaliscious 
# mainTrombonePitch = [REST, B2, B2, GS2, B2, GS2, REST, GS2, GS2, GS2, GS2, GS2, REST, GS2, GS2, GS2, GS2, GS2, E2, CS2, REST, GS2, GS2, GS2, GS2,
#                      FS2, FS2, FS2, FS2, GS2, REST, CS2, CS2, CS2, CS2, E2, E2, E2, E2, FS2, FS2, FS2, FS2, FS2, FS2, FS2, GS2, REST, B2, GS2, B2, GS2, B2, GS2, FS2, GS2]
# mainTromboneDurat = [EN,   SN, SN, EN,  EN, QN,  EN,   SN,  SN,  EN,  EN,  QN,  EN,   SN,  SN,  EN,  EN,  EN,  EN, QN,  EN,   SN,  SN,  EN,  EN,
#                      EN,  EN,  EN,  EN,  QN,  QN,   SN,  EN,  SN,  EN,  SN, EN, SN, EN, SN,  EN,  SN,  EN,  EN,  EN,  EN,  QN,  QN,   SN, EN,  SN, EN,  EN, QN,  HN,  DHN]
mainTrombonePitch = [[E4, E5], [G4, G5], [G4, G5], [E4, E5], [E4, E5], [C4, C5], REST, REST, [DS4, DS5], [E4, E5], [F4, F5], [B4, G5], [E4, E5], REST, REST, [G4, G5], [E4, E5], [D4, D5], [C4, C5], [GS3, GS4], [A3, A4], REST, REST, REST, [AS3, AS4], [B4, B5], [E4, E5], [D4, D5], [E4, E5], REST]
mainTromboneDurat = [QN,       EN,       SN,       SN,       EN,       SN,       SN,   SN,   SN,         SN,       SN,       DEN,      EN,       SN,   SN,   SN,       QN,       EN,       SN,       SN,         QN,       SN,   SN,   SN,   SN,         QN,       EN,       EN,       QN,       QN]
mainTrombonePhrase.addNoteList(mainTrombonePitch, mainTromboneDurat)
mainTrombonePhrase2.addNoteList(mainTrombonePitch, mainTromboneDurat)
Mod.repeat(mainTrombonePhrase, 4)
Mod.repeat(mainTrombonePhrase2, 6)
mainTromboneBeat.addPhrase(mainTrombonePhrase)
mainTromboneBeat2.addPhrase(mainTrombonePhrase2)


## Chorus
### Bass beat
electricBassChorus = Part(ELECTRIC_BASS, 4)
electricBassChorus.setTempo(180.0)
electricBassChorusPhrase = Phrase(179.0)

electricBassPitch =    [B2, E3, B2, A2, C3, E3, B2, REST, A2, A2, REST, B2, REST, A2, A2, F2]
electricBassDuration = [WN, HN, HN, QN, QN, QN, QN, QN,   QN, QN, QN,   HN, HN,   QN, QN, HN]
electricBassChorusPhrase.addNoteList(electricBassPitch, electricBassDuration)

Mod.repeat(electricBassChorusPhrase, 4)
electricBassChorus.addPhrase(electricBassChorusPhrase)

### Synth Beat
synthChorus = Part(SYNTH_BASS2, 11)
synthChorus.setTempo(80.0)
synthPhraseChorus = Phrase(79.1)

synthPitch = [F3, D3, E3, C3, REST, E3, G3, B3, E3, REST, D3, E3, C3, A2, REST, A2, A2, D3, F3, REST, E3, E3, A3, G3, REST, C3, A2, F3, A3, REST, A3, E3, D3, G3, REST, C3, A2, D3, G3, REST, C3, C3, A3, D3, C3, REST, REST, C3, C3, G3, B2, A2, REST, REST, D3, D3, A3, E3, B3, REST, REST, G2, G2, G2, E2, D3, REST, REST]
synthDurat = [SN, SN, SN, SN, QN] * 8 + [SN, SN, SN, SN, SN, SN, EN] * 4
synthPhraseChorus.addNoteList(synthPitch, synthDurat)

Mod.repeat(synthPhraseChorus, 2)
synthChorus.addPhrase(synthPhraseChorus)


## Composing full song

# Intro
original.addPart(trumpet1)
original.addPart(trumpet2)
original.addPart(horn)
original.addPart(trombone)

# Transition
original.addPart(drumsPart)
original.addPart(pizzicatoPart)

# Main 1
mainDrumPhrase.setDynamic(20)
original.addPart(mainDrumsPart)
original.addPart(electricBassPart)
mainTrombonePhrase.setDynamic(50)
original.addPart(mainTromboneBeat)

# Chorus
electricBassChorusPhrase.setDynamic(70)
original.addPart(electricBassChorus)
original.addPart(synthChorus)

# Repeat main after chorus
original.addPart(mainDrumsPart2)
original.addPart(electricBassPart2)
original.addPart(mainTromboneBeat2)
 
#View.sketch(original)
# Play.midi(original)
Write.midi(original, "Trial.mid")