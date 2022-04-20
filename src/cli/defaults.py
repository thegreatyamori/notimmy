import typing


class Defaults:
    trade: str = "SELL"
    country: str = "ecuador"
    payments: typing.List[str] = ['Produbanco']
    fetch_time: int = 10
    process_time: int = 30
    is_running: bool = True
