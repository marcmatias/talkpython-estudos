import os
from typing import List
import collections

SearchResult = collections.namedtuple('SearchResult', 'file, line, text')

def print_header():
    print('\n--------------------')
    print('     FILE SEARCH APP')
    print('--------------------\n')


def get_folder_from_user() -> None | str:
    folder = input('What folder do you want to search? ')

    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_search_text_from_user() -> str:
    text = input('What are you searching for [single phrases only]? ')
    return text


def search_folders(folder: str, text: str) -> List[str]:
    all_matches: List[str] = []
    items: List[str] = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(item):
            continue

        matches = search_file(full_item, text)
        all_matches.extend(matches)

    return all_matches


def search_file(filename: str, search_text: str):
    matches: List[str] = []
    with open(filename, 'r', encoding='utf-8') as fin:

        line_number = 0
        for line in fin:
            line_number += 1
            if line.lower().find(search_text) >= 0:
                m = SearchResult(line=line_number, file=filename, text=line)
                matches.append(m)

        return matches


def main() -> None:
    print_header()

    folder = get_folder_from_user()
    if not folder:
        print('''Sorry we can't search that location.''')
        return

    text = get_search_text_from_user()
    if not text:
        print('''Sorry we can't search for nothing!''')

    matches = search_folders(folder, text)
    for m in matches:
        print('---------- MATCH ----------')
        print(f'file: {m.file}')
        print(f'line: {m.line}')
        print(f'match: {m.text.rstrip()}\n')



if __name__ == '__main__':
    main()
