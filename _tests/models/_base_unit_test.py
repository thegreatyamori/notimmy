from datetime import datetime
from decimal import Decimal

from src.models._base import Model


class Person:
    id: int
    name: str
    lastname: str
    age: int = None
    weight: Decimal = None
    created_at: datetime
    updated_at: datetime


class TestModel:
    def test__generate_table_name__from_person(self):
        model_test = Model(Person)

        assert model_test.name == "person"

    def test__validate_data_types__from_person(self):
        expected_attributes = (
            "id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL",
            "name TEXT NOT NULL",
            "lastname TEXT NOT NULL",
            "age INTEGER NULL",
            "weight REAL NULL",
            "created_at TIMESTAMP NOT NULL",
            "updated_at TIMESTAMP NOT NULL",
        )

        model_test = Model(Person)

        assert model_test.attributes == expected_attributes
