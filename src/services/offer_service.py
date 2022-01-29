import sqlite3
import logging

from datetime import datetime

import src.storage as ds
from src.models.offer import model_offer


class OfferService:
    def __init__(self, connection: sqlite3.Connection):
        self.connection = connection
        self.cursor = connection.cursor()
        self.name = model_offer.name

        self.__create()

    def get(self):
        pass

    def insert(self, **params_values):
        created_at = (
            datetime.utcnow()
            if not params_values.get('created_at') else
            params_values.get('created_at')
        )
        _values = {
            **params_values,
            'updated_by': 'thegrbot',
            'created_at': created_at,
            'updated_at': datetime.utcnow(),
        }
        _attributes = model_offer.model.__annotations__.keys()

        values_as_tuple = tuple(_values.values())
        attributes_as_tuple = tuple(_values.keys())

        ds.insert_item(self.cursor, self.name, attributes_as_tuple, values_as_tuple)
        logging.info('insert data ...')

    def __create(self):
        ds.create_table(self.cursor, self.name, model_offer.attributes)
        logging.info('creating table ...')


c = OfferService(connection=ds.connect())
# c.insert(value=1.4563, created_by="thegrbot")
ds.commit(c.connection)
