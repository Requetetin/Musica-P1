# Savior (interlude).py
# Original song by Kendrick Lamar
# Spotify Link: https://open.spotify.com/track/5G4uLkFKdEZLcuNyeomQmE?si=390f575ea68546d8
 
from music import *

savior = Score("Savior (interlude)", 118)

violin1 = Part(VIOLIN, 0)
violin2 = Part(VIOLIN, 1)
viola = Part(VIOLA, 2)
cello = Part(CELLO, 3)
contrabass = Part(CONTRABASS, 4)

# Part 1
# Violin

violinPhrase = Phrase()

v1p1 = [F4, F4, F4, C4, F4, A4]
v1d1 = [WN, WN, QN, QN, QN, QN]

violinPhrase.addNoteList(v1p1, v1d1)
violin1.addPhrase(violinPhrase)

# Violin 2

violin2Phrase = Phrase()

v2p1 = [F4, C5, F4, REST, E4, B4, E4, REST, D4, A4, D4, REST]
v2d1 = [QN, QN, QN, QN,   QN, QN, QN, QN,   QN, QN, QN, QN]

violin2Phrase.addNoteList(v2p1, v2d1)
violin2.addPhrase(violin2Phrase)

# Viola

violaPhrase = Phrase()

vip1 = [C5, C5, C5, REST, B4, B4, B4, REST, A4, A4, A4, REST]
vid1 = [QN, QN, QN, QN,   QN, QN, QN, QN,   QN, QN, QN, QN]

violaPhrase.addNoteList(vip1, vid1)
viola.addPhrase(violaPhrase)

# Cello

celloPhrase = Phrase()

cp1 = [D4, REST, REST, D4, D4, REST, REST, D4, D4, REST, REST, D4]
cd1 = [QN, QN,   QN,   QN, QN, QN,   QN,   QN, QN, QN,   QN,   QN]

celloPhrase.addNoteList(cp1, cd1)
cello.addPhrase(celloPhrase)

# Contrabass

bassPhrase = Phrase()

bp1 = [D5, D5, D5]
bd1 = [WN, WN, WN]

bassPhrase.addNoteList(bp1, bd1)
contrabass.addPhrase(bassPhrase)

violinPhrase.setDynamic(20)
savior.addPart(violin1)
violin2Phrase.setDynamic(127)
savior.addPart(violin2)
violaPhrase.setDynamic(63)
savior.addPart(viola)
celloPhrase.setDynamic(63)
savior.addPart(cello)
bassPhrase.setDynamic(63)
savior.addPart(contrabass)
 
Play.midi(savior)