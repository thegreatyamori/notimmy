import json
import typing


class BinanceP2PParser():
    def __init__(self, data) -> None:
        self.data = data
        self.parsed_data = self.__parse_data()

    def __parse_data(self) -> typing.Dict:
        return json.loads(self.data)

    def get_info(self):
        return [
            {
                "price": trader["adv"]["price"],
                "surplusAmount": trader["adv"]["surplusAmount"],
                "maxSingleTransAmount": trader["adv"]["maxSingleTransAmount"],
                "minSingleTransAmount": trader["adv"]["minSingleTransAmount"],
                "tradeMethods": trader["adv"]["tradeMethods"],
                "nickName": trader["advertiser"]["nickName"]
            }
            for trader in self.parsed_data['data']
        ]