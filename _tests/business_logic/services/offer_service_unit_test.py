from datetime import datetime
from decimal import Decimal

import pytest

from src.business_logic.services.offer import OfferService


class TestOfferService:
    @pytest.fixture()
    def test_setup(self, mocker):
        def factory():
            service = OfferService()
            get_items_inside_range_mock = mocker.patch(
                'src.business_logic.daos.OfferDAO.get_items_inside_range'
            )
            insert_mock = mocker.patch('src.business_logic.daos.OfferDAO.insert')

            return mocker.Mock(
                service=service,
                get_items_inside_range=get_items_inside_range_mock,
                insert=insert_mock,
            )

        return factory

    def test__get_method_calls_dao_method__when_is_called(self, test_setup):
        setup = test_setup()
        expected_date_ranges = (datetime(2022, 1, 30, 13, 00), datetime(2022, 1, 30, 14, 00),)
        min_date_range, max_date_range = expected_date_ranges

        setup.service.get_many(min_date_range, max_date_range)

        setup.get_items_inside_range.assert_called_once_with(expected_date_ranges)

    def test__insert_method_calls_dao_method__when_is_called(self, test_setup):
        setup = test_setup()
        expected_value = Decimal(1.0005)

        setup.service.insert(expected_value)

        setup.insert.assert_called_once_with(value=expected_value)
