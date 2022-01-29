import decimal
from datetime import datetime
import re

_DATA_TYPES = {
    int: "INTEGER",
    float: "REAL",
    decimal.Decimal: "REAL",
    str: "TEXT",
    bytes: "BLOB",
    datetime: "TIMESTAMP",
}


class Model:
    def __init__(self, model: object):
        self.model = model
        self.name = None
        self.attributes = None

        self.__get_model_name()
        (
            self
            .__set_attributes_to_string()
            .__set_pk()
            .__set_null()
            .__get_attributes()
        )

    def __get_model_name(self):
        model_name = self.model.__name__
        self.name = self._to_snake_case(model_name)

    def __set_attributes_to_string(self):
        attributes = self.model.__annotations__
        self.attributes = [
            f"{_attr} {_DATA_TYPES[_type]}"
            for _attr, _type in attributes.items()
        ]
        return self

    def __set_pk(self):
        pk = "PRIMARY KEY AUTOINCREMENT"
        self.attributes[0] += f" {pk}"
        return self

    def __set_null(self):
        _model = self.model.__dict__
        _attributes = self.model.__annotations__
        _NULL = "NULL"
        _NOT_NULL = "NOT NULL"

        for position, _attr in enumerate(_attributes.keys()):
            try:
                if not _model[_attr]:
                    self.attributes[position] += f" {_NULL}"
            except KeyError:
                self.attributes[position] += f" {_NOT_NULL}"
        return self

    def __get_attributes(self):
        self.attributes = tuple(self.attributes)
        return self

    @staticmethod
    def _to_snake_case(model_name):
        return re.sub(r'(?<!^)(?=[A-Z])', '_', model_name).lower()
