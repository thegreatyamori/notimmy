from src.business_logic.services import P2PRetrieverService


class TestP2PRetrieverService:
    def test__request_calls_binance_p2p_api(self, mocker):
        trade_type = 'tradeType'
        pay_types = ['payTypes']
        country = 'country'
        request_mock = mocker.patch(
            'requests.post',
            return_value=mocker.Mock(text='{"data":[]}')
        )
        mocker.patch('src.business_logic.mappers.P2PMapper')
        expected_api_uri = 'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'

        service = P2PRetrieverService(trade_type, pay_types, country)
        service.fetch()

        assert request_mock.call_args.args[0] == expected_api_uri
        assert request_mock.called
