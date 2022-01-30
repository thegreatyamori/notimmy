import sqlite3
import logging
import typing

from datetime import datetime

import src.business_logic.storage as ds
from src.business_logic.models.offer import model_offer


def _build_items(retrieved_items: typing.List) -> typing.List[model_offer.model]:
    model_attrs = model_offer.model.__annotations__.keys()
    return [
        model_offer.model(
            **{attr: value for attr, value in zip(model_attrs, item)}
        ) for item in retrieved_items
    ]


class OfferDAO:
    def __init__(self, connection: sqlite3.Connection):
        self.connection = connection
        self.cursor = connection.cursor()
        self.name = model_offer.name

        self.__create()

    def get_items_inside_range(self, date_ranges) -> typing.List[model_offer.model]:
        filters = [f"{date_range}%" for date_range in date_ranges]
        retrieved_items = ds.retrieve_items(self.cursor, self.name, 'created_at', filters)
        logging.info('retrieving data...')

        return _build_items(retrieved_items)

    def insert(self, **params_values: typing.Dict):
        created_at = (
            datetime.utcnow()
            if not params_values.get('created_at') else
            params_values.get('created_at')
        )
        _values = {
            **params_values,
            'created_by': 'thegrbot',
            'updated_by': 'thegrbot',
            'created_at': created_at,
            'updated_at': datetime.utcnow(),
        }
        _attributes = model_offer.model.__annotations__.keys()

        values_as_tuple = tuple(_values.values())
        attributes_as_tuple = tuple(_values.keys())

        ds.insert_item(self.cursor, self.name, attributes_as_tuple, values_as_tuple)
        logging.info('inserting data...')

    def __create(self):
        ds.create_table(self.cursor, self.name, model_offer.attributes)
        logging.info('creating table...')
