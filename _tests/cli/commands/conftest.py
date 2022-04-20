import pytest


@pytest.fixture
def fake_run_command(mocker):
    mocks = mocker.Mock()

    mocks.process_and_notify = mocker.patch('src.business_logic.AppService.process_and_notify')
    mocks.fetch_and_save = mocker.patch('src.business_logic.AppService.fetch_and_save')
    mocks.execute_jobs = mocker.patch('src.business_logic.services.SchedulerService.execute_jobs')
    mocks.run_fetch_live_offers = mocker.patch(
        'src.business_logic.services.SchedulerService.run_fetch_live_offers'
    )
    mocks.run_process_live_offers = mocker.patch(
        'src.business_logic.services.SchedulerService.run_process_live_offers'
    )

    return mocks
