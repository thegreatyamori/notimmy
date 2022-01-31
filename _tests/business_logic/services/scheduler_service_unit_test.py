import pytest

from src.business_logic.services import SchedulerService


class TestSchedulerService:
    @pytest.fixture
    def test_setup(self, mocker):
        def factory():
            def _func(name):
                return f"Hello {name}"

            service = SchedulerService
            scheduler = mocker.patch('src.business_logic.services.scheduler.schedule')
            time = mocker.patch('src.business_logic.services.scheduler.time')

            return mocker.Mock(
                time=time,
                func=_func,
                service=service,
                scheduler=scheduler,
            )
        return factory

    def test__run_fetch_live_offers_calls_scheduler__every_15_minutes(self, mocker,test_setup):
        setup = test_setup()
        func = setup.func
        expected_calls = [mocker.call(15), mocker.call().minutes.do(func, "scheduler",)]

        setup.service.run_fetch_live_offers(func, 'scheduler')

        assert setup.scheduler.every.mock_calls == expected_calls

    def test__run_process_live_offers_calls_scheduler__every_30_minutes(self, mocker, test_setup):
        setup = test_setup()
        func = setup.func
        expected_calls = [mocker.call(30), mocker.call().minutes.do(func, name="scheduler",)]

        setup.service.run_process_live_offers(func, name='scheduler')

        assert setup.scheduler.every.mock_calls == expected_calls

    def test__execute_jobs_calls__run_pending_method(self, test_setup):
        setup = test_setup()

        setup.service.execute_jobs()

        assert setup.scheduler.run_pending.called
        assert setup.time.sleep.called
