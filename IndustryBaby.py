# Duplicate IndustryBaby.py
# Diego Alvarez
# Martin Amado
# Alejandra Gudiel
 
from music import *

industryBaby = Score("INDUSTRY BABY", 200)

trombone = Part(TROMBONE, 3)
trombone1n2Phrase = Phrase()

trombone1n2Pitch    = [ E3,   E3,   E3,   E3,   E3, E3, [B3, E3], [B3, E3], [B3, E3], [B3, E3], [B3, E3 ], [B3, E3 ], [E4, E3], [E4, E3], [E4, E3], [E4, E3], [E4, E3], [E4, E3], E3  ]  
trombone1n2Duration = [ QN, 0.33, 0.33, 0.33,   QN, QN,       QN,     0.33,     0.33,     0.33,        QN,        QN,       QN,     0.33,     0.33,     0.33,       QN,       QN, WN  ] 

trombone1n2Phrase.addNoteList(trombone1n2Pitch, trombone1n2Duration)

trombone.addPhrase(trombone1n2Phrase)
industryBaby.addPart(trombone)

trombone1n2Phrase.setTempo(144) 

Play.midi(industryBaby)
# Write.midi(industryBaby, "Trial.mid")