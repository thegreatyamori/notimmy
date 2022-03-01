import typing


class Defaults(object):
    trade: typing.Optional[str] = "SELL"
    country: typing.Optional[str] = "ecuador"
    payments: typing.Optional[typing.List[str]] = ['Produbanco']
    fetch_time: typing.Optional[int] = 10
    process_time: typing.Optional[int] = 30
