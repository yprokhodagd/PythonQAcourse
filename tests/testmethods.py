import json
from pprint import pprint

import requests


def get_book_by_type(type):
    URL = f"http://127.0.0.1:5000/v1/books/ids?book_type={type}"
    x = requests.get(URL)
    return x.text


def get_book_by_id(id):
    URL = f'http://127.0.0.1:5000/v1/books/info?id={id}'
    x = requests.get(URL)
    return x.text


def get_book_latest(limit):
    URL = f"http://127.0.0.1:5000/v1/books/latest?limit={limit}"
    x = requests.get(URL)
    return x.text


def add_book(type, title, creation_date):
    """
    :param type: only following:
        Science_Fiction = "Science"
        Satire = "Satire"
        Drama = "Drama"
        Action_and_Adventure = "Adventure"
        Romance = "Romance"
    :param title: any str, not more 255
    :param creation_date: any str with format like: '2000-01-01'
    :return:
    """
    url = 'http://127.0.0.1:5000/v1/books/manipulation'
    payload = {'type': type,
               'title': title,
               'creation_date': creation_date
               }

    headers = {'content-type': 'application/json'}
    data = json.dumps(payload)
    x = requests.post(url, data=data, headers=headers)
    return x.text


def delete_book(id):
    url = f'http://127.0.0.1:5000/v1/books/manipulation?id={id}'
    x = requests.delete(url)
    return x.text


def update_book(id, type, title):
    url = f'http://127.0.0.1:5000/v1/books/manipulation?id={id}'
    payload = {'type': type,
               'title': title}
    headers = {'content-type': 'application/json'}
    data = json.dumps(payload)
    x = requests.put(url, data=data, headers=headers)  #, headers=headers)
    return x.text
