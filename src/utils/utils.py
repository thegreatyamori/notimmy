from decimal import Decimal
from functools import reduce


def average_for_many_values(*numbers):
    _numbers = [Decimal(number) for number in numbers]
    accumulate_value = reduce(lambda x, y: x+y, _numbers)

    return round(accumulate_value / len(_numbers), 4)
