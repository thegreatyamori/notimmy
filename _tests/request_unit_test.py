from src.request_data import request_p2p_data


def test__request_calls_binance_p2p_api(mocker):
    # setup
    trade_type = 'tradeType'
    pay_types = ['payTypes']
    transaction_amount = 0
    request_mock = mocker.patch(
        'requests.post',
        return_value=mocker.Mock(text='{"data":[]}')
    )
    mocker.patch('src.services.parser_service.BinanceP2PParser')

    # execute
    request_p2p_data(trade_type, pay_types, transaction_amount)

    # assert
    assert request_mock.call_args[0] == ('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search',)
    request_mock.assert_called()
