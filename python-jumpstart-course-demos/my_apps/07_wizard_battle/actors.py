import random

class Creature:
    name: str
    level: int


    def __init__(self, name: str, level: int) -> None:
        self.name = name
        self.level = level

    def __repr__(self) -> str:
        return f'Creature {self.name} of level {self.level}'

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):
    name: str
    level: int


    def __init__(self, name: str, level: int) -> None:
        super().__init__(name, level)

    def __repr__(self) -> str:
        return f'Wizard {self.name} of level {self.level}'

    def attack(self, creature: Creature) -> bool:
        print(f'The wizard {self.name} attacks {creature.name}!')

        my_roll = self.get_defensive_roll()
        creature_roll = creature.get_defensive_roll()

        print(f'You roll {my_roll}...')
        print(f'{creature.name} rolls {creature_roll}')

        if my_roll >= creature_roll:
            print(f'The wizard has handily triumphed over {creature.name}.')
            return True
        else:
            print('The wizard has been DEFEATED!!1')
            return False


class SmallAnimal(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll / 2


class Dragon(Creature):
    scaliness: int

    def __init__(self, name: str, level: int, scaliness: int, breaths_fire: bool) -> None:
        super().__init__(name, level)
        self.scaliness = scaliness
        self.breaths_fire = breaths_fire

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        fire_modifier = 5 if self.breaths_fire else 1
        scale_modifier = self.scaliness / 10
        return base_roll * fire_modifier * scale_modifier
