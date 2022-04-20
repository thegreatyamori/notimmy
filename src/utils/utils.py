import typing
from datetime import datetime, timedelta
from decimal import Decimal
from functools import reduce


def average_for_many_values(*numbers):
    """
    calculates the average value for the 3 best P2P offers plus ideal sales value.
    numbers: a tuple of values
    """
    _numbers = [Decimal(number) for number in numbers]
    accumulate_value = reduce(lambda x, y: x + y, _numbers)

    return round(accumulate_value / len(_numbers), 4)


def calculate_last_time(minutes_to_subtract: int) -> typing.Tuple[datetime, datetime]:
    now = datetime.utcnow()
    time_to_subtract = timedelta(minutes=minutes_to_subtract)

    return now - time_to_subtract, now
