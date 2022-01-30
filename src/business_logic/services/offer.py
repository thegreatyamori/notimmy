from src.business_logic.daos import OfferDAO
from src.business_logic.storage import connect


class OfferService:
    def __init__(self):
        self.dao = OfferDAO(connection=connect())

    def get(self, min_date_range, max_date_range):
        date_range = (min_date_range, max_date_range,)

        return self.dao.get_items_inside_range(date_range)

    def insert(self, offer_value):
        self.dao.insert(value=offer_value)
