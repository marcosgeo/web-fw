# conftest.py

import os
import pytest

from bumbo.api import API
from bumbo.orm import Database, Table, Column, ForeignKey



@pytest.fixture
def api():
    return API()


@pytest.fixture
def client(api):
    return api.test_session()


@pytest.fixture
def db():
    db_file = "./orm_test.db"
    if os.path.exists(db_file):
        os.remove(db_file)
    db = Database(db_file)
    return db


@pytest.fixture
def Author():
    class Author(Table):
        name = Column(str)
        age = Column(int)

    return Author


@pytest.fixture
def Book(Author):
    class Book(Table):
        title = Column(str)
        published = Column(bool)
        author = ForeignKey(Author)

    return Book

