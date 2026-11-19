import random

class Creature:
    name: str
    level: int


    def __init__(self, name: str, level: int) -> None:
        self.name = name
        self.level = level


    def __repr__(self) -> str:
        return f'Creature {self.name} of level {self.level}'


class Wizard:
    name: str
    level: int


    def __init__(self, name: str, level: int) -> None:
        self.name = name
        self.level = level


    def __repr__(self) -> str:
        return f'Wizard {self.name} of level {self.level}'


    def attack(self, creature: Creature) -> bool:
        print(f'The wizard {self.name} attacks {creature.name}!')

        my_roll = random.randint(1, 12) * self.level
        creature_roll = random.randint(1, 12) * creature.level

        print(f'You roll {my_roll}...')
        print(f'{creature.name} rolls {creature_roll}')

        if my_roll >= creature_roll:
            print(f'The wizard has handily triumphed over {creature.name}.')
            return True
        else:
            print('The wizard has been DEFEATED!!1')
            return False
