
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
class BirdFoto:
    id      :   int
    url     :   str
    descroption :   str | None = None


@dataclass
class Bird:
    id              : int
    short_name      : str
    size            : int   # BirdSize.id
    
    sc_class        : int | None    = None # BirdClass.id
    latin_name      : str | None    = None
    english_name    : str | None    = None
    aliases         : list[str] | None     = None
    dascription     : str | None    = None

    foto_main       : int | None    = None # BirdFoto.id
    foto_male       : int | None    = None # BirdFoto.id
    foto_female     : int | None    = None # BirdFoto.id
    album           : list[int] | None    = None # list[BirdFoto.id]

    tags            : list[int] | None     = None   # list[BirdTags.id]


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
        BirdSize(0, 'bullfinch', 'small then bullfinch'),   # снегирь
        BirdSize(1, 'jay', 'small then jay'),               # сойка
        BirdSize(2, 'raven', 'small then a raven'),         # ворон
        BirdSize(3, 'heron', 'big bird'),                   # цапля
        ]

birds = [Bird(1, 'sparrow', 0),
         Bird(2, 'crow', 2)]

