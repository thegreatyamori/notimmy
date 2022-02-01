import decimal

from src.business_logic.services import (
    NotifierService,
    OfferService,
    P2PRetrieverService,
    SchedulerService,
)
from src.utils import average_for_many_values, calculate_last_time


_TYPE_OF_TRADE = 'SELL'
_FILTER_BY_PAYMENT = ["Produbanco"]
_COUNTRY = "ecuador"
_DEFAULT_FETCH_TIME = 15
_DEFAULT_PROCESS_TIME = 31


class AppService:
    def __init__(self):
        self._notifier_service = NotifierService
        self._p2p_retriever_service = P2PRetrieverService(
            _TYPE_OF_TRADE, _FILTER_BY_PAYMENT, _COUNTRY
        )
        self.scheduler_service = SchedulerService(_DEFAULT_FETCH_TIME, _DEFAULT_PROCESS_TIME)

    def run_fetch_task(self):
        def fetch_and_save():
            offer_service = OfferService()
            offers = self._p2p_retriever_service.fetch()

            min_bid_value = average_for_many_values(*(offer['price'] for offer in offers[:3]))
            offer_service.insert(str(min_bid_value))
            offer_service.commit_changes()

        self.scheduler_service.run_fetch_live_offers(fetch_and_save)

    def run_notify_task(self):
        def process_and_notify():
            offer_service = OfferService()
            offers = self._p2p_retriever_service.fetch()

            time = calculate_last_time(self.scheduler_service.process_time)
            get_last_offers = offer_service.get_many(*time)
            offer_service.commit_changes()

            min_bid_value = average_for_many_values(*(offer.value for offer in get_last_offers))

            for offer in offers[:3]:
                price = offer['price']
                if price > decimal.Decimal(min_bid_value):
                    trade_methods = [trade['payType'] for trade in offer['tradeMethods']]
                    title = f"@{offer['nickName']} trades for {price} !"
                    msg = (
                        f"{offer['surplusAmount']} "
                        f"({offer['minSingleTransAmount']} - {offer['maxSingleTransAmount']})\n"
                        f"{','.join(trade_methods)}"
                    )
                    notifier = self._notifier_service(title, msg)
                    notifier.display()

        self.scheduler_service.run_process_live_offers(process_and_notify)
