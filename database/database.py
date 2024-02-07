#!/usr/bin/env python3

from dataclasses import dataclass




@dataclass
class BirdsTags:
    tag:str
    descr:str = None


@dataclass
class Bird:
    short_name  :   str
    size_class  :   int
    latin_name  :   str | None= None
    description :   str | None= None
    album       :   str | None= None
    main_photo  :   str | None= None
    tags        :   list[BirdsTags] | None = None


birds = [Bird('sparrow', 1), Bird('crown', 3)]



def save_birds(filename: str, *birds: Bird):
    with open(filename + '.py', 'w') as f:
        print('birds = [', file=f)
        for b in birds:
            print(b.__dict__, ',', file=f)
        print(']', file=f)


def load_birds(filename:str):
    #module = __import__('.' +filename)
#    import .dbb
#    print(module.birds)
    return birds


if __name__ == '__main__':
    save_birds('dbb', *birds)

