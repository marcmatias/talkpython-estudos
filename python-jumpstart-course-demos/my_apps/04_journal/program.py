import journal

def header():
    print('--------------------')
    print('     JOURNAL APP')
    print('--------------------')
    print()


def run_event_loop():
    print('What do you want to do with your journal?')
    cmd = 'EMPTY'
    journal_name = 'default'
    journal_data = journal.load(journal_name)

    while cmd != 'x' and cmd:
        cmd = input('[L]ist entries, [A]dd and entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and cmd:
            print(f'Sorry, we don\'t understand {cmd}')
    journal.save(journal_name, journal_data)
    print('Done, end')


def list_entries(data):
    if len(data):
        print('Your journal entries')
        entries = reversed(data)
        for i, entry in enumerate(entries):
            print(f'{i+1}: {entry}')
    else:
        print('Nothing to be showed')


def add_entry(data):
    text = input('Type your entry, <Enter> to exit: ')
    data.append(text)


if __name__ == '__main__':
    header()
    run_event_loop()
