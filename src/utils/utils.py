from decimal import Decimal
from functools import reduce


def average_for_many_values(*numbers) -> Decimal:
    """
    calculates the average value for the 3 best P2P offers plus ideal sales value.
    numbers: a tuple of values
    """
    _numbers = [Decimal(number) for number in numbers]
    accumulate_value = reduce(lambda x, y: x+y, _numbers)

    return Decimal(round(accumulate_value / len(_numbers), 4))
