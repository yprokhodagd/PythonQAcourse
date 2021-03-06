import json
import pytest
from pprint import pprint

from tests.testmethods import add_book, get_book_by_type, get_book_by_id, get_book_latest, delete_book, update_book
from tests.book import Book

book1 = Book('Science', 'Title1', '2021-01-01')
book2 = Book('Science', 'Title2', '2022-01-01')


@pytest.mark.parametrize('book', [book1, book2])
def test_add_book(book):
    res = add_book(book.type, book.title, book.date)
    print(res)
    res = json.loads(res)
    assert res['title'] == book.title, f"Title verification: expected: {book.title}, actual: {res['title']}"
    assert res['type'] == book.type, f"Type verification: expected: {book.type}, actual: {res['type']}"
    assert res['creation_date'] == book.date, f"Type verification: expected: {book.date}, actual: {res['type']}"


@pytest.mark.parametrize('book', [book1, book2])
def test_delete_book(book):
    res_add = add_book(book.type, book.title, book.date)
    res_add = json.loads(res_add)
    res_add_id = res_add['id']

    res = delete_book(id=res_add_id)
    res = json.loads(res)
    assert res['title'] == book.title, f"Title verification: expected: {book.title}, actual: {res['title']}"
    assert res['type'] == book.type, f"Type verification: expected: {book.type}, actual: {res['type']}"
    assert res['creation_date'] == book.date, f"Type verification: expected: {book.date}, actual: {res['type']}"


@pytest.mark.parametrize('book', [book1, book2])
def test_update_book(book):
    res_add = add_book(book.type, book.title, book.date)
    res_add = json.loads(res_add)
    res_add_id = res_add['id']

    changed_type = 'Satire'
    changed_title = 'Title_changed'
    res = update_book(id=res_add_id, type=changed_type, title=changed_title)
    res = json.loads(res)

    assert res['id'] == res_add_id, f"ID verification: expected: {res_add_id}, actual: {res['id']}"
    assert res['type'] == changed_type, f"Type verification: expected: {changed_type}, actual: {res['type']}"
    assert res['title'] == changed_title, f"Title verification: expected: {changed_title}, actual: {res['title']}"
    assert res['creation_date'] == book.date, f"Type verification: expected: {changed_type}, actual: {res['type']}"


@pytest.mark.parametrize('book', [book1, book2])
def test_get_book_by_type(book):
    add_book(book.type, book.title, book.date)
    res = get_book_by_type(type=book.type)
    res = json.loads(res)
    assert res[-1]['title'] == book.title, f"Title verification: expected: {book.title}, actual: {res[-1]['title']}"
    assert res[-1]['type'] == book.type, f"Type verification: expected: {book.type}, actual: {res[-1]['type']}"
    assert res[-1]['creation_date'] == book.date, f"Creation date verification: expected: {book.date}, " \
                                                  f"actual: {res[-1]['creation_date']}"


@pytest.mark.parametrize('book', [book1, book2])
def test_get_book_by_id(book):
    res_add = add_book(book.type, book.title, book.date)
    res_add = json.loads(res_add)
    res_add_id = res_add['id']

    res = get_book_by_id(id=res_add_id)
    res = json.loads(res)

    assert res['title'] == book.title, f"Title verification: expected: {book.title}, actual: {res['title']}"
    assert res['type'] == book.type, f"Type verification: expected: {book.type}, actual: {res['type']}"
    assert res['creation_date'] == book.date, f"Creation date verification: expected: {book.date}, " \
                                              f"actual: {res['creation_date']}"


def test_get_book_latest():
    add_book(book1.type, book1.title, book1.date)
    add_book(book2.type, book2.title, book2.date)

    res = get_book_latest(limit=2)
    res = json.loads(res)
    pprint(res)

    assert res[0]['title'] == book2.title, f"Title verification: expected: {book2.title}, actual: {res[0]['title']}"
    assert res[0]['type'] == book2.type, f"Type verification: expected: {book2.type}, actual: {res[0]['type']}"
    assert res[0]['creation_date'] == book2.date, f"Creation date verification: expected: {book2.date}, " \
                                                  f"actual: {res[0]['creation_date']}"

    assert res[1]['title'] == book1.title, f"Title verification: expected: {book1.title}, actual: {res[1]['title']}"
    assert res[1]['type'] == book1.type, f"Type verification: expected: {book1.type}, actual: {res[1]['type']}"
    assert res[1]['creation_date'] == book1.date, f"Creation date verification: expected: {book1.date}, " \
                                                  f"actual: {res[1]['creation_date']}"
