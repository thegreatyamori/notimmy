import pytest

from src.business_logic.daos.offer import OfferDAO


@pytest.fixture(name='fake_connection')
def _fake_connection(mocker):
    return mocker.patch('src.business_logic.storage.connect')


class TestOfferDAO:
    @pytest.fixture()
    def test_setup(self, mocker, fake_connection):
        def factory():
            dao = OfferDAO(connection=fake_connection)
            log = mocker.patch('src.business_logic.daos.offer.logging')
            retrieve_items = mocker.patch('src.business_logic.storage.retrieve_items')
            insert_item = mocker.patch('src.business_logic.storage.insert_item')
            create_table = mocker.patch('src.business_logic.storage.create_table')

            return {
                'dao': dao,
                'log': log,
                'retrieve_items': retrieve_items,
                'insert_item': insert_item,
                'create_table': create_table,
            }

        return factory

    def test__shows_log_message__when_item_was_retrieved(self, mocker, test_setup):
        setup = test_setup()
        dao = setup['dao']
        log = setup['log']
        date_ranges = tuple()
        expected_msg = 'retrieving data...'

        dao.get_items_inside_range(date_ranges)

        assert log.info.called
        assert log.info.call_args == mocker.call(expected_msg)

    def test__calls_retrieve_items__when_get_method_is_called(self, test_setup):
        setup = test_setup()
        dao = setup['dao']
        retrieve_items = setup['retrieve_items']
        date_ranges = tuple()

        dao.get_items_inside_range(date_ranges)

        retrieve_items.assert_called_once_with(dao.cursor, dao.name, 'created_at', [])

    def test__shows_log_message__when_item_was_inserted(self, mocker, test_setup):
        setup = test_setup()
        dao = setup['dao']
        log = setup['log']
        param_values = {
            'value': mocker.sentinel.value
        }
        expected_msg = 'inserting data...'

        dao.insert(**param_values)

        assert log.info.called
        assert log.info.call_args == mocker.call(expected_msg)

    def test__calls_insert_item__when_insert_method_is_called(self, mocker, test_setup):
        setup = test_setup()
        dao = setup['dao']
        insert_item = setup['insert_item']
        param_values = {
            'value': mocker.sentinel.value,
            'created_by': mocker.sentinel.created_by
        }
        expected_name = 'offer'
        expected_attributes = ('value', 'created_by', 'updated_by', 'created_at', 'updated_at')

        dao.insert(**param_values)

        assert insert_item.called
        assert insert_item.call_args.args[0:3] == (dao.cursor, expected_name, expected_attributes)
