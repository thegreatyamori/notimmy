import requests

from src.business_logic.mappers import P2PMapper


_DEFAULT_CURRENCY = "USDT"


class P2PRetrieverService:
    __base_url = "p2p.binance.com"

    def __init__(self, trade_type, pay_types, transaction_amount=0, asset=_DEFAULT_CURRENCY):
        self.trade_type = trade_type
        self.pay_types = pay_types
        self.transaction_amount = transaction_amount
        self.asset = asset

    def retrieve(self):
        headers = self.__set_headers()
        data = self.__build_data()
        api_url = f"https://{self.__base_url}/bapi/c2c/v2/friendly/c2c/adv/search"
        response = requests.post(api_url, headers=headers, json=data)
        map_data = P2PMapper(response.text)

        return map_data.execute()

    def __build_data(self):
        return {
            "asset": self.asset,
            "payTypes": self.pay_types,
            "tradeType": self.trade_type,
            "transAmount": self.transaction_amount,
            "page": 1,
            "rows": 10,
            "order": '',
            "fiat": "USD",
            "filterType": 'all',
            "publisherType": None,
            "countryType": 'ecuador',
        }

    def __set_headers(self):
        return {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Length": "123",
            "content-type": "application/json",
            "Host": self.__base_url,
            "Origin": f"https://{self.__base_url}",
            "Pragma": "no-cache",
            "TE": "Trailers",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"
        }
