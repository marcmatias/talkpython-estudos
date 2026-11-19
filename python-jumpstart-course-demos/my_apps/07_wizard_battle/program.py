from actors import Wizard, Creature
import random
import time

def print_header():
    print()
    print('--------------------')
    print('     WIZARD BATTLE')
    print('--------------------')
    print()


def game_loop():

    creatures = [
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Creature('Bat', 3),
        Creature('Dragon', 50),
        Creature('Evil Wizard', 100),
    ]

    hero = Wizard('Gandalf', 75)

    while True:
        active_creature = random.choice(creatures)
        print(f'A {active_creature.name} of level {active_creature.level} has appear from a dark and foggy forest...')

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print('The wizard runs and hides taking time to recover...')
                time.sleep(5)
                print('The wizard returns revitalized!')
        elif cmd ==  'r':
            print('runaway')
        elif cmd == 'l':
            print(f'The wizard {hero.name} takes in the surroundings and sees: ')
            for c in creatures:
                print(f' * A {c.name} level {c.level}')
        else:
            print('OK, exiting game... bye!')
            break

        if not creatures:
            print()
            print('''You've defeated all the creatures , well done!''')
            print()
            print('Bye!')
            break


def main():
    print_header()
    game_loop()


if __name__ == '__main__':
    main()
