from decimal import Decimal

from src.utils import average_for_many_values, calculate_last_time
from .notifier import NotifierService
from .offer import OfferService
from .p2p_retriever import P2PRetrieverService


class AppService:
    def __init__(self, defaults):
        self._notifier_service = NotifierService
        self._p2p_retriever_service = P2PRetrieverService(
            defaults.trade, defaults.payments, defaults.country
        )
        self.process_time = defaults.process_time

    def fetch_and_save(self):
        offer_service = OfferService()
        offers = self._p2p_retriever_service.fetch()

        min_bid_value = average_for_many_values(*(offer.price for offer in offers[:3]))
        offer_service.insert(str(min_bid_value))
        offer_service.commit_changes()

    def process_and_notify(self):
        offer_service = OfferService()
        offers = self._p2p_retriever_service.fetch()

        time = calculate_last_time(self.process_time)
        get_last_offers = offer_service.get_many(*time)
        offer_service.commit_changes()

        min_bid_value = average_for_many_values(*(offer.value for offer in get_last_offers))

        for offer in offers[:3]:
            price = offer.price
            if price > Decimal(min_bid_value):
                title = f"@{offer.nickName} trades for {price} !"
                msg = (
                    f"{offer.surplusAmount} "
                    f"({offer.minSingleTransAmount} - {offer.maxSingleTransAmount})\n"
                    f"{', '.join([trade['payType'] for trade in offer.tradeMethods])}"
                )
                notifier = self._notifier_service(title, msg)
                notifier.display()
