import sqlite3
import os
import typing

_DB_NAME = 'p2p_system.db'
_BASE_PATH = "../../../"


def connect():
    os.chdir(_BASE_PATH)
    _base_path = os.getcwd()

    return sqlite3.connect(f"{_base_path}/{_DB_NAME}")


def create_table(cursor: sqlite3.Cursor, table_name: str, attributes: tuple):
    build_query = f"CREATE TABLE IF NOT EXISTS {table_name} {attributes};"
    clean_query = build_query.replace("'" or '"', "")

    return cursor.execute(clean_query)


def insert_item(cursor: sqlite3.Cursor, table_name: str, attributes: tuple, values: tuple):
    build_query = (
        "INSERT INTO {table_name} {attributes} "
        "VALUES (?,?,?,?,?);"
    ).format(table_name=table_name, attributes=attributes)

    return cursor.execute(build_query, values)


def retrieve_items(cursor: sqlite3.Cursor, table_name: str, column: str, filters: typing.Tuple):
    build_query = (
        "SELECT * FROM {table_name} "
        "WHERE {column} > ? AND {column} < ?"
    ).format(table_name=table_name, column=column)

    return cursor.execute(build_query, filters).fetchall()


def commit(connection: sqlite3.Connection):
    connection.commit()
    # connection.close()