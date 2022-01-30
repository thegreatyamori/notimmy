import pytest
import src.business_logic.services.notifier as notifier_service


@pytest.fixture()
def mock_dependencies(mocker):
    return {
        'notify': mocker.patch('src.services.notifier_service.Notify')
    }


def test__show_simple_notification__when_display_method_is_called(mock_dependencies):
    params = {
        'title': 'hello',
        'message': 'world',
    }

    notifier = notifier_service.NotifierService(**params)
    notifier.display()

    assert mock_dependencies['notify'].return_value.title == params['title']
    assert mock_dependencies['notify'].return_value.message == params['message']
    mock_dependencies['notify'].assert_called()
    mock_dependencies['notify'].return_value.send.assert_called()
