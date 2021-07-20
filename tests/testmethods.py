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


if __name__ == "__main__":
    pass
    # print(test_get_book_by_type())
    # pprint(test_get_book_by_id("ce0372e8-90df-45fc-85c4-5db1b1c02549"))
    # print(test_delete_book(book_id="9884bb39-eeea-477d-8297-500c3f708588"))
    # print(add_book(book_type='Science', title='title', creation_date='2021-01-02'))
    # print(test_update_book(book_id="599d13b2-0897-443e-8aec-630cc0a1beaa", type='Science', title='title111',))
    pprint(get_book_latest(10))
