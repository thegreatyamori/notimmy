import sqlite3
import typing

_DB_NAME = 'p2p_system.db'


def connect():
    return sqlite3.connect(_DB_NAME)


def create_table(cursor: sqlite3.Cursor, table_name: str, attributes: tuple):
    build_query = f"CREATE TABLE IF NOT EXISTS {table_name} {attributes};"
    clean_query = build_query.replace("'" or '"', "")

    return cursor.execute(clean_query)


def insert_item(cursor: sqlite3.Cursor, table_name: str, attributes: tuple, values: tuple):
    build_query = f"INSERT INTO {table_name} {attributes} VALUES (?,?,?,?,?);"
    return cursor.execute(build_query, values)


def retrieve_items(cursor: sqlite3.Cursor, table_name: str, column: str, filters: typing.List):
    build_query = (
        "SELECT * FROM {table_name} "
        "WHERE {column} > ? AND {column} < ?"
    ).format(table_name=table_name, column=column)

    return cursor.execute(build_query, filters).fetchall()


def commit(connection: sqlite3.Connection):
    connection.commit()
    connection.close()
