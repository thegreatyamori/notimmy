import decimal
import re
from datetime import datetime

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

        self._get_model_name()
        (
            self
                ._set_attributes_to_string()
                ._set_pk()
                ._set_null()
                ._get_attributes()
        )

    def _get_model_name(self):
        model_name = self.model.__name__
        self.name = self._to_snake_case(model_name)

    def _set_attributes_to_string(self):
        attributes = self.model.__annotations__
        self.attributes = [
            f"{_attr} {_DATA_TYPES[_type]}"
            for _attr, _type in attributes.items()
        ]
        return self

    def _set_pk(self):
        _pk = "PRIMARY KEY AUTOINCREMENT"
        self.attributes[0] += f" {_pk}"
        return self

    def _set_null(self):
        _model = self.model.__dict__
        _attributes = self.model.__annotations__
        _null = "NULL"
        _not_null = "NOT NULL"

        for position, _attr in enumerate(_attributes.keys()):
            try:
                if not _model[_attr]:
                    self.attributes[position] += f" {_null}"
            except KeyError:
                self.attributes[position] += f" {_not_null}"
        return self

    def _get_attributes(self):
        self.attributes = tuple(self.attributes)
        return self

    @staticmethod
    def _to_snake_case(model_name):
        return re.sub(r'(?<!^)(?=[A-Z])', '_', model_name).lower()
