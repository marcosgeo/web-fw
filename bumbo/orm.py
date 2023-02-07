# bumbo/orm.py

import inspect
import sqlite3


class Database:
    def __init__(self, path):
        self.conn = sqlite3.Connection(path)

    @property
    def tables(self):
        SELECT_TABLES_SQL = "SELECT name FROM sqlite_master WHERE type = 'table';"
        return [ x[0] for x in self.conn.execute(SELECT_TABLES_SQL).fetchall() ]

    def create(self, table):
        self.conn.execute(table._get_create_sql())


class Table:
    @classmethod
    def _get_create_sql(cls):
        CREATE_TABLE_SQL = "CREATE TABLE IF NOT EXISTS {name} ({fields});"
        fields_lst = [
            "id INTEGER PRIMARY KEY AUTOINCREMENT",
        ]
        for name, field in inspect.getmembers(cls):
            if isinstance(field, Column):
                fields_lst.append(f"{name.lower()} {field.sql_type}")
            elif isinstance(field, ForeignKey):
                fields_lst.append(f"{name.lower()}_id INTEGER")
        fields_str = ", ".join(fields_lst)
        name = cls.__name__.lower()
        return CREATE_TABLE_SQL.format(name=name, fields=fields_str)


class Column:
    def __init__(self, column_type):
        self.type = column_type

    @property
    def sql_type(self):
        SQLITE_TYPE_MAP = {
            int: "INTEGER",
            float: "REAL",
            str: "TEXT",
            bytes: "BLOB",
            bool: "INTEGER",
        }
        return SQLITE_TYPE_MAP[self.type]


class ForeignKey:
    def __init__(self, table):
        self.table = table


