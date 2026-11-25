import os
import movie_svc
import requests


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def print_header():
    clear_screen()
    print('------------------')
    print(' Movie Search APP')
    print('------------------\n')


def search_event_loop():
    search = 'ONCE_THROUGH_LOOP'

    while search != 'x':
        try:
            try:
                search = input('Movie search text {x to exit}: ')
            except KeyboardInterrupt:
                print('\nExiting..\n')
                return
            if search != 'x':
                results = movie_svc.find_movies(search)
                print(f'Found {len(results)} reults.')
                for r in results:
                    print(f'{r.year} -- {r.title}')
                print()
        except requests.exceptions.ConnectionError as ce:
            print(f'\nConection error with API. Details: {ce}\n')
        except Exception as e:
            print(f'\nAn error occurred. Details: {e}\n')
    print('Exiting..\n')


def main():
    print_header()
    search_event_loop()


if __name__ == '__main__':
    main()
