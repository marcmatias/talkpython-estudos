import cat_service
import os
import platform
import subprocess


def print_header():
    print()
    print('--------------------')
    print('     CAT FACTORY')
    print('--------------------')
    print()


def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pictures'
    full_path = os.path.join(base_folder, folder)

    # Não existe ou não é um diretório, para o caso de um arquivo com o mesmo nome que quermeos dar à pasta existir no diretório
    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print(f'Creating new directory at {full_path}')
        os.mkdir(full_path)

    return full_path


def download_cats(folder):
    print('Contacting server to download cats...')
    cat_count = 8
    for i in range(1, cat_count+1):
        name = f'lolcat_{i}'
        print(f'Dowloading cat {name}')
        cat_service.get_cat(folder, name)
    print('done.')


def display_cats(folder):
    print('Displaying cats in OS window')
    system = platform.system()
    if system == 'Darwin':
        subprocess.call(['open', folder])
    elif system == 'Windows':
        subprocess.call(['explorer', folder])
    elif system == 'Linux':
        subprocess.call(['xdg-open', folder])
    else:
        print('''We don't support your OS''')


def main():
    print_header()
    folder = get_or_create_output_folder()
    download_cats(folder)
    display_cats(folder)


if __name__ == '__main__':
    main()
