import os
import requests
import collections

MovieResult = collections.namedtuple('MovieResult',
                                     'imdb_code,title,duration,director,year,rating,imdb_score,keywords,genres')

search = input('What movie do you want to search for? ')
url = f'https://movieservice.talkpython.fm/api/search/{search}'
response = requests.get(url)

# Raise response if something went wrong
response.raise_for_status()

movie_data = response.json()
movies_list = movie_data.get('hits')

# movies = []

# for md in movies_list:
#     m = MovieResult(**md)
#     movies.append(m)


movies = [MovieResult(**md) for md in movies_list]

os.system('clear')

print(f'Found {len(movies)} movies for search {search}\n')

for m in movies:
    print(f'{m.year} -- {m.title}')

print()
