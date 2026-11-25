import collections
import requests

MovieResult = collections.namedtuple('MovieResult',
                                     'imdb_code,title,duration,director,year,rating,imdb_score,keywords,genres')


def find_movies(search_text):
    if not search_text or not search_text.strip():
        raise ValueError('Search text required')

    url = f'https://movieservice.talkpython.fm/api/search/{search_text}'

    response = requests.get(url)
    response.raise_for_status()

    movies_data = response.json()
    movies_list = movies_data.get('hits')

    movies = [MovieResult(**md) for md in movies_list]

    movies.sort(key=lambda m: -m.year)

    return movies
