# Duplicate IndustryBaby.py
# Diego Alvarez
# Martin Amado
# Alejandra Gudiel
 
from music import *

industryBaby = Score("INDUSTRY BABY", 200)

trombone = Part(TROMBONE, 3)
trombone1n2Phrase = Phrase()

trumpet = Part(TRUMPET, 4)
trumpet1n2Phrase = Phrase()

clarinet = Part(CLARINET, 5)
clarinet1n2Phrase = Phrase()

altoSax1n2 = Part(ALTO_SAX, 6)
altoSax1n2Phrase = Phrase()

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

trumpet1n2Pitch = [   REST, REST, REST, REST
                    , [F5, C5], REST,    [E5, B4], REST,    [F5, C5], REST,    REST, [C5, A4], [E5, F5], [F5, C5]
                    , [F5, C5], REST,    [E5, B4], REST,    [F5, C5], REST,    REST, [C5, F4], [C5, F4], [C5, F4], [C5, F4], [C5, F4], [C5, F4]
                    , [F5, C5], [E5, B4], REST,    REST, [C5, F4], [C5, F4], [C5, F4], [C5, F4], [C5, F4], [C5, F4],    [F5, A4], [C5, F4], REST,    [F5, B4], [F5, B4], [G5, C5], [G5, C5], [A5, DF5], [G5, CF5], [F5, BF5], [E5, AF5]
                    ]
trumpet1n2Duration = [WN, WN, WN, WN
                    , DHN, QN, DHN, QN, DHN, QN, QN, QN, QN, QN
                    , DHN, QN,         DHN, QN,             DHN, QN,           QN,   EN,       EN,       EN,       EN,       EN,       EN
                    , QN, QN, HN,                  QN,    EN,      EN,       EN,       EN,       EN,       EN,          QN,       QN,       HN,      EN,       EN,       EN,        EN,      EN,         EN,        EN,       EN
                    ]
trumpet1n2Phrase.addNoteList(trumpet1n2Pitch, trumpet1n2Duration)

clarinet1n2Pitch = [   REST, REST, REST, REST
                    , [F5, C5], REST,    [E5, B4], REST,    [F5, C5], REST,    [C5, A4], [E5, B4], [F5, C5]
                    , [F5, C5], REST,    [E5, B4], REST,    [F5, C5], REST,    REST, [C5, F4], [C5, F4], [C5, F4], [C5, F4], [C5, F4], [C5, F4]
                    , [F5, C5], [E5, B4], REST, REST, [C5, F4], [C5, F4], [C5, F4], [C5, F4], [C5, F4], [C5, F4], [F5, A4], [C5, F4], REST, [F5, B4], [F5, B4], [G5, C5], [G5, C5], [A5, DF5], [G5, CF5], [F5, BF5], [E5, AF5]
                    ]
clarinet1n2Duration = [WN, WN, WN, WN
                    , DHN, QN,           DHN, QN,            DHN,     QN,       QN, QN, QN
                    , DHN, QN,           DHN, QN,            DHN,     QN,       QN, EN, EN, EN, EN, EN, EN
                    , QN, QN, HN,               QN,    EN,        EN,     EN,        EN,       EN,      EN,        QN,      QN,        HN,  EN,       EN,       EN,        EN,      EN,         EN,        EN,        EN
                    ]
clarinet1n2Phrase.addNoteList(clarinet1n2Pitch, clarinet1n2Duration)

altoSax1n2Pitch = [ REST, REST, REST, REST
                    , E5, D5, E5, F5, E5, REST, E5, D5, C5, REST, C5, D5, E5
                    , E5, D5, E5, F5, E5, REST, E5, D5, C5, REST, C5, D5, E5
                    , E5, D5, E5, F5, E5, REST, E5, D5, C5, REST, C5, D5, E5
                    ]
altoSax1n2Duration = [ WN, WN, WN, WN
                    , EN, EN, HN, EN, EN, WN, EN, EN, DHN, QN, QN, QN, QN
                    , EN, EN, HN, EN, EN, WH, EN, EN, DHN, QN, QN, QN, QN
                    , EN, EN, HN, EN, EN, WN, EN, EN, DHN, QN, QN, QN, QN
                    ]
altoSax1n2Phrase.addNoteList(altoSax1n2Pitch, altoSax1n2Duration)

#Page_2
trombone1n2Pitch    = [  G3, F3, G3, A3, G3, F3, G3, F3,  E3, REST, E3, F3, G3
                       , G3, F3, G3, A3, G3, F3, G3, F3,  E3, REST, E3, F3, G3
                       , G3, F3, G3, A3, G3, F3, G3, F3,  E3, REST, E3, F3, G3
                       , G3, F3, G3, A3, G3, F3  ]
trombone1n2Duration = [  EN, EN, HN, EN, EN, WN, EN, EN, DHN,   QN, QN, QN, QN
                       , EN, EN, HN, EN, EN, WN, EN, EN, DHN,   QN, QN, QN, QN
                       , EN, EN, HN, EN, EN, WN, EN, EN, DHN,   QN, QN, QN, QN
                       , EN, EN, HN, EN, EN, WN  ]
trombone1n2Phrase.addNoteList(trombone1n2Pitch, trombone1n2Duration)

trumpet1n2Pitch = [ [F5, B5], [E5, A4], REST, REST, [C5, G4], [C5, G4], [C5, G4], [C5, G4], [C5, G4], [C5, G4], [F5, A4], [C5, F4], REST, REST
                    , REST, REST, REST, REST
                    , REST, REST, REST, REST, C6, C6, C6, B5, B5, A5
                    , B5, A5, B5, A5, B5, A5, F5, REST, C6, C6, C6, B5, B5, A5
                    ]
trumpet1n2Duration = [ QN, QN, HN, QN, EN, EN, EN, EN, EN, EN, QN, QN, HN, WN
                    , WH, WH, WH, WH
                    , WH, WH, WH, QN, EN, EN, EN, EN, EN, EN
                    , EN, EN, EN, EN, EN, EN, QN, QN, EN, EN, EN, EN, EN, EN
                    ]
trumpet1n2Phrase.addNoteList(trumpet1n2Pitch, trumpet1n2Duration)

clarinet1n2Pitch = [ [F5, B4], [E5, A4], REST, REST, [C5, G4], [C5, G4], [C5, G4], [C5, G4], [C5, G4], [C5, G4], [F5, A4], [C5, F4], REST, REST 
                    , REST, REST, REST, REST
                    , REST, REST, REST, REST, C6, C6, C6, B5, B5, A5
                    , B5, A5, B5, A5, B5, A5. F5, REST, C6, C6, C6, B5, B5, A5
                    ]
clarinet1n2Duration = [  QN, QN, HN, QN, EN, EN, EN, EN, EN, EN, QN, QN, HN, WN
                    , WH, WH, WH, WH
                    , WH, WH, WH, QN, EN, EN, EN, EN, EN, EN
                    , EN, EN, EN, EN, EN, EN, QN, QN, EN, EN, EN, EN, EN, EN
                    ]
clarinet1n2Phrase.addNoteList(clarinet1n2Pitch, clarinet1n2Duration)

altoSax1n2Pitch = [ E5, D5, E5, F5, E5, REST, E5, D5, C5, REST, C5, D5, E5
                    , G5, F5, E5, F5, E5, D5, D5, D5, D5, D5, E5, D5, C5, REST, C5, D5, E5
                    , G5, F5, E5, F5, E5, D5, D5, D5, D5, D5, E5, D5, C5, REST, G5, G5, G5, F5, F5, E5
                    , F5, E5, F5, E5, F5, E5, C5, REST, G5, G5, G5, F5, F5, E5
                    ]
altoSax1n2Duration = [EN, EN, HN, EN, EN, WN, EN, EN, DHN, QN, QN, QN, QN
                    , EN, EN, HN, EN, EN, HN, EN, EN, EN, EN, EN, EN, DHN, QN, QN, QN, QN
                    , EN, EN, HN, EN, EN, HN, EN, EN, EN, EN, EN, EN, DHN, QN, EN, EN, EN, EN, EN, EN
                    , EN, EN, EN, EN, EN, EN, QN, QN, EN, EN, EN, EN, EN, EN
                    ]
altoSax1n2Phrase.addNoteList(altoSax1n2Pitch, altoSax1n2Duration)

#Page_3

trombone1n2Pitch    = [ G3, F3,  E3, REST, E3, F3, G3, REST, REST
                        , REST, REST, REST, REST
                        , REST, REST, REST, REST
                        , REST,  G3, F3, G3, A3, G3, REST]
trombone1n2Duration = [ EN, EN, DHN,   QN, QN, QN, QN,   WN,   WN
                        ,   WN,   WN,   WN,   WN
                        ,   WN,   WN,   WN,   WN
                        ,   WN,   EN, EN, HN, EN, EN, WN]
trombone1n2Phrase.addNoteList(trombone1n2Pitch, trombone1n2Duration)

trumpet1n2Pitch = [B5, A5, B5, A5, B5, C6, C6, REST, F5, G5, A5, C6, B5, A5, B5, A5, G5, G5, G5, G5, G5,G5
                    , A5, G5, F5, F5, E5, F5, REST, REST
                    , REST, REST, REST, REST
                    , REST, REST, REST, REST]
trumpet1n2Duration = [EN, EN, EN, EN, EN, EN, QN, QN, QN, QN, QN, EN, EN, HN, EN, EN, DQN, EN, EN, EN, EN, EN
                    , EN, EN, HN, EN, EN, QN, QN, HN, WN, WN
                    , WN, WN, WN, WN
                    , WN, WN, WN, WN]
trumpet1n2Phrase.addNoteList(trumpet1n2Pitch, trumpet1n2Duration)

clarinet1n2Pitch = [ B5, A5, B5, A5, B5, C6, C6, REST, F5, G5, A5, C6, B5, A5, B5, A5, G5, G5, G5, G5, G5,G5
                    , A5, G5, F5, F5, E5, F5, REST, REST
                    , REST, REST, REST, REST
                    , REST, REST, REST, REST
                    ]
clarinet1n2Duration = [ EN, EN, EN, EN, EN, EN, QN, QN, QN, QN, QN, EN, EN, HN, EN, EN, DQN, EN, EN, EN, EN, EN
                    , EN, EN, HN, EN, EN, QN, QN, HN, WN, WN
                    , WN, WN, WN, WN
                    , WN, WN, WN, WN
                    ]
clarinet1n2Phrase.addNoteList(clarinet1n2Pitch, clarinet1n2Duration)

altoSax1n2Pitch = [ F5, E5, F5, E5, F5, G5, G5, REST, C5, D5, E5, G5, F5, E5, F5, E5, D5, D5, D5, D5, D5, D5
                    , A5, G5, F5, F5, E5, F5, REST, REST
                    , REST , REST, REST, REST
                    , REST, REST, REST, REST
                    ]
altoSax1n2Duration = [ EN, EN, EN, EN, EN, EN, QN, QN, QN, QN, QN, EN, EN, HN, EN, EN, DQN, EN, EN, EN, EN, EN
                    , EN, EN, HN, EN, EN, QN, QN, HN, WN, WN
                    , WN, WN, WN, WN
                    , WN, WN, WN, WN
                    ]
altoSax1n2Phrase.addNoteList(altoSax1n2Pitch, altoSax1n2Duration)

#Page_4

trombone1n2Pitch    = [   G3, F3,  E3,  REST, E3, F3, G3,  G3, F3, G3, A3, G3, REST
                        , G3, F3, E3, REST, G3, F3, G3, A3, G3, REST
                        , G3, F3, E3, REST, E3, F3, G3, G3, F3, G3, A3, G3, REST
                        , G3, F3, E3, REST, E3, F3, G3, G3, F3, G3, A3, G3, REST ]
trombone1n2Duration = [   EN, EN,   DHN, QN, QN, QN, QN,  EN, EN, HN, EN, EN, WN
                        , EN, EN, DHN, WN, EN, EN, HN, EN, EN, WN
                        , EN, EN, DHN, QN, QN, QN, QN, EN, EN, HN, EN, EN, WN
                        , EN, EN, DHN, QN, QN, QN, QN, EN, EN, HN, EN, EN, WN]
trombone1n2Phrase.addNoteList(trombone1n2Pitch, trombone1n2Duration)

# trumpet1n2Pitch = []
# trumpet1n2Duration = []
# trumpet1n2Phrase.addNoteList(trumpet1n2Pitch, trumpet1n2Duration)

#Page_5

trombone1n2Pitch    = [   G3, F3,  E3, REST, E3, F3, G3, G3, F3, G3, A3, G3, REST
                        , G3, F3,  E3, REST, E3, F3, G3, G3, F3, G3, A3, G3, REST
                        , G3, F3, E3, REST, E3, F3, G3, REST, REST
                        , REST, REST, E3, F3, G3]
trombone1n2Duration = [   EN, EN, DHN, QN, QN, QN, QN, EN, EN, HN, EN, EN, WN
                        , EN, EN, DHN, QN, QN, QN, QN, EN, EN, HN, EN, EN, WN
                        , QN, QN, DHN, QN, QN, QN, QN, WN, WN
                        , WN, QN, QN, QN, QN]
trombone1n2Phrase.addNoteList(trombone1n2Pitch, trombone1n2Duration)

# trumpet1n2Pitch = []
# trumpet1n2Duration = []
# trumpet1n2Phrase.addNoteList(trumpet1n2Pitch, trumpet1n2Duration)

#Page_6

trombone1n2Pitch    = [   G3, F3,  G3, A3, G3, REST, G3, F3, E3, REST, E3, F3, G3
                        , G3, F3, G3, A3, G3, REST, G3, F3, E3, REST, E3, F3, G3]
trombone1n2Duration = [   EN, EN, HN, EN, EN, WN, EN, EN, DHN, QN, QN, QN, QN
                        , EN, EN, HN, EN, EN, WN, EN, EN, DHN, QN, QN, QN, QN]
trombone1n2Phrase.addNoteList(trombone1n2Pitch, trombone1n2Duration)

# trumpet1n2Pitch = []
# trumpet1n2Duration = []
# trumpet1n2Phrase.addNoteList(trumpet1n2Pitch, trumpet1n2Duration)

trombone.addPhrase(trombone1n2Phrase)
industryBaby.addPart(trombone)

trombone1n2Phrase.setTempo(144) 

trumpet.addPhrase(trumpet1n2Phrase)
industryBaby.addPart(trumpet)

trumpet1n2Phrase.setTempo(144) 

clarinet.addPhrase(clarinet1n2Phrase)
industryBaby.addPart(clarinet)

clarinet1n2Phrase.setTempo(144)

altoSax1n2.addPhrase(altoSax1n2Phrase)
industryBaby.addPart(altoSax1n2)

altoSax1n2Phrase.setTempo(144)

Play.midi(industryBaby)
# Write.midi(industryBaby, "Trial.mid")