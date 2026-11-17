'''
This is the journal module.
'''

import os

def load(name):
    '''
    This methods creates and load a new journal.

    :param name: This base name of the journal to load.
    :return: A new jorunal data structure propulated with the file data
    '''
    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                print('would load: ' + entry.rstrip())
                data.append(entry.rstrip())

    return data


def save(name, journal_data):
    filename = os.path.abspath(os.path.join('./journals/', name + '.jrl'))
    print(f'....... saving to: {filename}')
    fout = open(filename, 'w')

    for entry in journal_data:
        fout.write(entry + '\n')

    fout.close()

def add_entry(text, journal_data):
    journal_data.append(text)

def get_full_pathname(name):
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))
    return filename
