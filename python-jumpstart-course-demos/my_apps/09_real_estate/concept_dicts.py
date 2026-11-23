import collections

# Dict uses keys instead of numbers

lookup = {}
lookup = dict()
lookup = { 'age': 42, 'loc': 'Italy' }
lookup = dict(age=42, loc='Italy')

class Wizard:
    def __init__(self, name: str, level: int):
        self.name = name
        self.level = level

gandolf = Wizard('Gandalf', 42)
print(gandolf.__dict__)

print(lookup)
print(lookup['loc'])

lookup['cat'] = 'Nina'

if 'cat' in lookup:
    print(lookup['cat'])

User =  collections.namedtuple('User', 'id, name, email')
users = [
    User(1, 'user1', 'user1@talkpython.fm'),
    User(2, 'user2', 'user2@talkpython.fm'),
    User(3, 'user3', 'user3@talkpython.fm'),
    User(4, 'user4', 'user4@talkpython.fm')
]

lookup = dict()
for u in users:
    lookup[u.email] = u

print(f'\nlookup: {lookup}\n')
print(lookup['user3@talkpython.fm'])
