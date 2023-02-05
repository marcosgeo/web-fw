# test_orm.py

import sqlite3

from bumbo.orm import Database


def test_create_db():
    db = Database("./orm_test.db")

    assert isinstance(db.conn, sqlite3.Connection)
    assert db.tables == []



