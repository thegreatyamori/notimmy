from src.request_p2p_data import request_P2P_data


def test_request_calls_binance_p2p_api(mocker):
    tradeType = 'tradeType'
    payTypes = ['payTypes']
    transactionAmount = 0
    request_mock = mocker.patch('src.request_p2p_data.requests.post', return_value=mocker.Mock(
        text='{"data":[]}'
    ))
    mocker.patch('src.services.parser_service.BinanceP2PParser')

    request_P2P_data(tradeType, payTypes, transactionAmount)

    assert request_mock.call_args[0] == ('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search',)
    request_mock.assert_called()