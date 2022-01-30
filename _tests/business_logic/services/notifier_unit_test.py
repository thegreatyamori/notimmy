from src.business_logic.services import NotifierService


def test__show_simple_notification__when_display_method_is_called(mocker):
    params = {
        'title': 'hello',
        'message': 'world',
    }
    notify_mock = mocker.patch('src.business_logic.services.notifier.Notify')

    notifier = NotifierService(**params)
    notifier.display()

    assert notify_mock.return_value.title == params['title']
    assert notify_mock.return_value.message == params['message']
    assert notify_mock.called
    assert notify_mock.return_value.send.called
