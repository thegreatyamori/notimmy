import decimal
import typing

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
_DEFAULT_FETCH_TIME = 1
_DEFAULT_PROCESS_TIME = 2


def _get_offers() -> typing.Tuple[OfferService, typing.List[typing.Dict]]:
    service = OfferService()
    p2p_retriever_service = P2PRetrieverService(_TYPE_OF_TRADE, _FILTER_BY_PAYMENT, _COUNTRY)

    offers = p2p_retriever_service.fetch()
    return service, offers


def _build_notification_skeleton(offer) -> typing.Tuple[str, str]:
    nickname = offer['nickName']
    price = offer['price']
    amount = offer['surplusAmount']
    min_amount = offer['minSingleTransAmount']
    max_amount = offer['maxSingleTransAmount']

    title = f"@{nickname} trades for {price}!"
    message = f"{amount} ({min_amount} - {max_amount})\n"
    return title, message


class AppService:
    def __init__(self):
        self._notifier_service = NotifierService
        self.scheduler_service = SchedulerService(_DEFAULT_FETCH_TIME, _DEFAULT_PROCESS_TIME)

    def run_fetch_task(self):
        self.scheduler_service.run_fetch_live_offers(self._fetch_and_save)

    def run_notify_task(self):
        self.scheduler_service.run_process_live_offers(self._process_and_notify)

    # noinspection PyMethodMayBeStatic
    def _fetch_and_save(self):
        service, offers = _get_offers()

        min_bid_value = str(average_for_many_values(*(offer['price'] for offer in offers[:3])))
        service.insert(min_bid_value)
        service.commit_changes()

    def _process_and_notify(self):
        service, offers = _get_offers()

        time = calculate_last_time(self.scheduler_service.process_time)
        get_last_offers = service.get_many(*time)
        service.commit_changes()

        min_bid_value = average_for_many_values(*(offer.value for offer in get_last_offers))

        for offer in offers[:3]:
            if offer['price'] > decimal.Decimal(min_bid_value):
                notifier = self._notifier_service(*_build_notification_skeleton(offer))
                notifier.display()
