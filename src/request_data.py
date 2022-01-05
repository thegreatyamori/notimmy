import requests

from .services.parser_service import BinanceP2PParser

def request_P2P_data(tradeType, payTypes, transactionAmount=0):
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Length": "123",
        "content-type": "application/json",
        "Host": "p2p.binance.com",
        "Origin": "https://p2p.binance.com",
        "Pragma": "no-cache",
        "TE": "Trailers",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"
    }
    data = {
        "asset": "USDT",
        "tradeType": tradeType,
        "fiat": "USD",
        "transAmount": transactionAmount,
        "order": '',
        "publisherType": None,
        "page": 1,
        "rows": 10,
        "countryType": 'ecuador',
        "filterType": 'all',
        "payTypes": payTypes
    }
    api_url = 'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'
    response = requests.post(
        api_url,
        headers=headers,
        json=data
    )
    binance_parser = BinanceP2PParser(response.text)

    return binance_parser.get_info()
