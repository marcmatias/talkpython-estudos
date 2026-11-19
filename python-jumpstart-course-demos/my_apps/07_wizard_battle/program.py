from actors import Wizard, Creature, SmallAnimal, Dragon
import random
import time

def print_header():
    print('\n--------------------')
    print('     WIZARD BATTLE')
    print('--------------------\n')


def game_loop():

    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, 20, True),
        Wizard('Evil Wizard', 100),
    ]

    hero = Wizard('Gandalf', 75)

    while True:
        active_creature = random.choice(creatures)
        print(f'A {active_creature.name} of level {active_creature.level} has appear from a dark and foggy forest...')

        try:
            cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')
        except KeyboardInterrupt:
            exiting_game_msg()
            break

        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                try:
                    print('The wizard runs and hides taking time to recover... We need to wait...')
                    time.sleep(5)
                    print('The wizard returns revitalized!')
                except KeyboardInterrupt:
                    exiting_game_msg()
                    break
        elif cmd ==  'r':
            print('runaway')
        elif cmd == 'l':
            print(f'The wizard {hero.name} takes in the surroundings and sees: ')
            for c in creatures:
                print(f' * A {c.name} level {c.level}')
        else:
            exiting_game_msg()
            break

        if not creatures:
            print('''\nYou've defeated all the creatures , well done!''')
            print('Bye!')
            break


def exiting_game_msg():
    print('OK, exiting game... bye!')


def main():
    print_header()
    game_loop()


if __name__ == '__main__':
    main()
