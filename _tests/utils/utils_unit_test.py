import pytest

from decimal import Decimal
from src.utils.utils import average_for_many_values


@pytest.mark.parametrize(
    "values, average", [
        ((1.021, 1.012, 1.008), 1.0137),
        ((1.02, 1.01), 1.015),
    ]
)
def test_average_for_many_values__returns_a_decimal_result(values, average):
    average_expected = round(Decimal(average), 4)
    average_result = average_for_many_values(*values)

    assert average_expected == average_result