#  pylint:disable=cyclic-import
from datetime import datetime
from decimal import Decimal

import pytest

from src.utils import average_for_many_values, calculate_last_time


@pytest.mark.parametrize(
    "values, average", [
        ((1.021, 1.012, 1.008), 1.0137),
        ((1.02, 1.01), 1.015),
    ]
)
def test__average_for_many_values__returns_a_decimal_result(values, average):
    average_expected = round(Decimal(average), 4)
    average_result = average_for_many_values(*values)

    assert average_result == average_expected


@pytest.mark.parametrize(
    "minutes, expected_ranges", [
        (40, (
            datetime(2022, 1, 30, 9, 20, 59),
            datetime(2022, 1, 30, 10, 00, 59),
        )),
        (26, (
            datetime(2022, 1, 30, 9, 34, 59),
            datetime(2022, 1, 30, 10, 00, 59),
        )),
        (59, (
            datetime(2022, 1, 30, 9, 1, 59),
            datetime(2022, 1, 30, 10, 00, 59),
        )),
    ]
)
def test__calculate_last_time__returns_a_tuple_of_datetime(mocker, minutes, expected_ranges):
    d_t = mocker.patch('src.utils.utils.datetime')
    d_t.utcnow = mocker.Mock(return_value=datetime(2022, 1, 30, 10, 00, 59))
    ranges = calculate_last_time(minutes_to_subtract=minutes)

    assert ranges == expected_ranges

#  pylint:enable=cyclic-import
