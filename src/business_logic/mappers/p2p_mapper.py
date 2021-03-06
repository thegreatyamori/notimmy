import json
import typing
from decimal import Decimal


class P2PMapper:
    def __init__(self, data) -> None:
        self.data = data
        self.parsed_data = self.__parse_data()

    def __parse_data(self) -> typing.Dict:
        return json.loads(self.data)

    def execute(self):
        return [
            {
                "nickName": trade_offer["advertiser"]["nickName"],
                "price": Decimal(trade_offer["adv"]["price"]),
                "surplusAmount": trade_offer["adv"]["surplusAmount"],
                "maxSingleTransAmount": trade_offer["adv"]["dynamicMaxSingleTransAmount"],
                "minSingleTransAmount": trade_offer["adv"]["minSingleTransAmount"],
                "tradeMethods": trade_offer["adv"]["tradeMethods"]
            }
            for trade_offer in self.parsed_data['data']
        ]
