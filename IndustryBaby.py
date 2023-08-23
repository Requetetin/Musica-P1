# Duplicate IndustryBaby.py
# Diego Alvarez
# Martin Amado
# Alejandra Gudiel
 
from music import *

industryBaby = Score("INDUSTRY BABY", 200)

trombone = Part(TROMBONE, 3)
trombone1n2Phrase = Phrase()

#Page_1
trombone1n2Pitch    = [ E3,   E3,   E3,   E3,   E3, E3, [B3, E3], [B3, E3], [B3, E3], [B3, E3], [B3, E3 ], [B3, E3 ], [E4, E3], [E4, E3], [E4, E3], [E4, E3], [E4, E3], [E4, E3], E3
                       , REST, B3, A3, B3, REST, REST, G3, REST, B3, A3, B3, REST,  G3, REST, REST, B3, A3, B3, A3, G3, G3, REST, B3, A3, B3, REST,  G3, REST
                       , REST, B3, A3, B3, REST, REST, G3, REST, B3, A3, B3, REST,  G3, REST, REST, B3, A3, B3, REST,  G3, REST, REST
                       , G3, F3, G3, A3, G3, F3, G3, F3,  E3, REST, E3, F3, G3  ]  
trombone1n2Duration = [ QN, 0.33, 0.33, 0.33,   QN, QN,       QN,     0.33,     0.33,     0.33,        QN,        QN,       QN,     0.33,     0.33,     0.33,       QN,       QN, WN
                       ,   QN, EN, EN, EN,   SN,   SN, EN,   QN, EN, EN,  EN,   SN,  EN,  SN,   QN, EN, EN, EN, EN, EN, EN,    SN, EN, EN, EN,   EN,  EN,   SN
                       ,   QN, EN, EN, EN,   SN,   SN, EN,   QN, EN, EN,  EN,   SN,  EN,  SN,   QN, EN, EN,  EN,   SN,  EN,  SN, WN
                       , EN, EN, HN, EN, EN, WN, EN, EN, DHN,   QN, QN, QN, QN  ] 

trombone1n2Phrase.addNoteList(trombone1n2Pitch, trombone1n2Duration)

#Page_2
trombone1n2Pitch    = [ G3, F3, G3, A3, G3, F3, G3, F3,  E3, REST, E3, F3, G3 ]
trombone1n2Duration = [ EN, EN, HN, EN, EN, WN, EN, EN, DHN,   QN, QN, QN, QN ]

trombone1n2Phrase.addNoteList(trombone1n2Pitch, trombone1n2Duration)


trombone.addPhrase(trombone1n2Phrase)
industryBaby.addPart(trombone)

trombone1n2Phrase.setTempo(144) 

Play.midi(industryBaby)
# Write.midi(industryBaby, "Trial.mid")