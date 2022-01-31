import datetime
import typing

from src.business_logic.daos import OfferDAO
from src.business_logic.storage import connect, commit


class OfferService:
    def __init__(self):
        self.dao = OfferDAO(connection=connect())

    def get_many(
            self,
            min_date_range: datetime.datetime,
            max_date_range: datetime.datetime
    ) -> typing.List:
        date_range = (min_date_range, max_date_range,)
        return self.dao.get_items_inside_range(date_range)

    def insert(self, offer_value):
        self.dao.insert(value=offer_value)

    def commit_changes(self):
        commit(self.dao.connection)
