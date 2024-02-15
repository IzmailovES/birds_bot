
from dataclasses import dataclass

@dataclass
class BirdTag:
    id          :   int
    name        :   str
    descr       :   str | None = None


@dataclass
class BirdSize:
    id      :   int
    name    :   str
    descr   :   str 

@dataclass
class BirdClass:
    id      :   int
    order   :   str
    family  :   str
    genus   :   str
    species :   str

@dataclass
class Bird:
    id              : int
    name            : str
    size            : int   # BirdSize.id
    
    sc_class        : int | None    = None # BirdClass.id
    latin_name      : str | None    = None
    english_name    : str | None    = None
    aliases         : list[str] | None     = None
    dascription     : str | None    = None

    foto_main       : str | None    = None
    foto_male       : str | None    = None
    foto_female     : str | None    = None
    album           : str | None    = None

    tags            : list[int] | None     = []    # list[BirdTags.id]


### next database hardcode!!!!

bird_tags = [
        BirdTag(0, 'color'),
        BirdTag(1, 'boring'),
        BirdTag(2, 'black'),
        BirdTag(3, 'predator'),
        BirdTag(4, 'peaceful'),
        BirdTag(5, 'regular'),
        BirdTag(6, 'rare'),
        BirdTag(7, 'migrate'),
        ]

bird_sizes = [
        BirdSize(0, 'bullfinch', 'small then bullfinch'),
        BirdSize(1, 'jay', 'small then jay'),
        BirdSize(2, 'crow', 'small then a big crown'),
        BirdSize(3, 'heron', 'big bird'),
        ]

birds = [


        ]

