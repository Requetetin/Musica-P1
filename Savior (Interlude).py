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

v1p1 = [F4, F4, F4, C4, F4, A4, G4, C4, C4, C4, C4, F4, A4, G4, C4]
v1d1 = [WN, WN, QN, QN, QN, QN, HN, HN, WN, WN, HN, QN, QN, HN, HN]

violinPhrase.addNoteList(v1p1, v1d1)
violin1.addPhrase(violinPhrase)

# Violin 2

violin2Phrase = Phrase()

v2p1 = [F4, C5, F4, REST, E4, B4, E4, REST, D4, A4, D4, REST, C4, G4, C4, REST, C4, F4, C4, REST, C4, A4, C4, REST, C4, G4, C4, REST, E4, F4, E4, REST]
v2d1 = [QN] * 4 * 8

violin2Phrase.addNoteList(v2p1, v2d1)
violin2.addPhrase(violin2Phrase)

# Viola

violaPhrase = Phrase()

vip1 = [C5, C5, C5, REST, B4, B4, B4, REST, A4, A4, A4, REST, G4, G4, G4, REST, F4, F4, G4, REST, G4, G4, G4, REST, G4, G4, G4, REST, F4, F4, F4, REST]
vid1 = [QN] * 4 * 8

violaPhrase.addNoteList(vip1, vid1)
viola.addPhrase(violaPhrase)

# Cello

celloPhrase = Phrase()

cp1 = [D4, REST, REST, D4, D4, REST, REST, D4, D4, REST, REST, D4, D4, REST, REST, D4, D4, REST, REST, D4, D4, REST, REST, D4, D4, REST, REST, D4, D4, REST, REST, G4]
cd1 = [QN] * 4 * 8

celloPhrase.addNoteList(cp1, cd1)
cello.addPhrase(celloPhrase)

# Contrabass

bassPhrase = Phrase()

bp1 = [D5, D5, D5, D5, D4, D4, D4, D4,  G4]
bd1 = [WN, WN, WN, WN, WN, WN, WN, DHN, QN]

bassPhrase.addNoteList(bp1, bd1)
contrabass.addPhrase(bassPhrase)


#Part 2
# Violin

violinPhrase = Phrase()

v1p1 = []
v1d1 = []

violinPhrase.addNoteList(v1p1, v1d1)
violin1.addPhrase(violinPhrase)

# Violin 2

violin2Phrase = Phrase()

v2p1 = []
v2d1 = []

violin2Phrase.addNoteList(v2p1, v2d1)
violin2.addPhrase(violin2Phrase)

# Viola

violaPhrase = Phrase()

vip1 = []
vid1 = []

violaPhrase.addNoteList(vip1, vid1)
viola.addPhrase(violaPhrase)

# Cello

celloPhrase = Phrase()

cp1 = []
cd1 = []

celloPhrase.addNoteList(cp1, cd1)
cello.addPhrase(celloPhrase)

# Contrabass

bassPhrase = Phrase()

bp1 = []
bd1 = []

bassPhrase.addNoteList(bp1, bd1)
contrabass.addPhrase(bassPhrase)



# Adding everything together

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
Write.midi(savior, "Savior.mid")