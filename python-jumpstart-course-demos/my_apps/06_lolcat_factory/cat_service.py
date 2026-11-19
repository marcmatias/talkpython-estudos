import os
import requests
import shutil

def get_cat(folder, name):
    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
    data = get_data_from_url(url)
    # print(f'get_cat {folder}_{name}', data)
    save_image(folder, name, data)
    pass


def get_data_from_url(url):
    response = requests.get(url, stream=True)
    return response.raw # binary string of data


def save_image(folder, name, data):
    file_name = os.path.join(folder, name + '.jpg')
    with open(file_name, 'wb') as fout: # fout e o nome do stream de saída
        shutil.copyfileobj(data, fout)
