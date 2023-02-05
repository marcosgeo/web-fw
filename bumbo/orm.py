# bumbo/orm.py

import sqlite3


class Database:
    def __init__(self, path):
        self.conn = sqlite3.Connection(path)

    @property
    def tables(self):
        return []


