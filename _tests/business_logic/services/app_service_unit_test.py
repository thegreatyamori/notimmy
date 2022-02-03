import typing

import pytest

from src.business_logic.services.app import AppService, _get_offers


class TestAppService:
    @pytest.fixture
    def test_setup(self, mocker):
        def factory(
                fetch_service=False,
                process_service=False,
        ):
            mocker.patch('src.business_logic.services.NotifierService')
            offer_service = mocker.patch(
                'src.business_logic.services.OfferService'
            )
            p2p_retriever_service = mocker.patch(
                'src.business_logic.services.P2PRetrieverService.fetch'
            )

            if fetch_service:
                fetch_scheduler_service = mocker.patch(
                    'src.business_logic.services.SchedulerService.run_fetch_live_offers',
                )

            if process_service:
                process_scheduler_service = mocker.patch(
                    'src.business_logic.services.SchedulerService.run_process_live_offers',
                )

            return mocker.Mock(
                offer_service=offer_service,
                p2p_retriever_service=p2p_retriever_service,
                fscheduler_service=fetch_scheduler_service if fetch_service else mocker.Mock(),
                pscheduler_service=process_scheduler_service if process_service else mocker.Mock(),
            )

        return factory

    def test__get_offers_method_dont_generates_the_same_class_instance__when_are_called_two_times(
            self,
            test_setup,
    ):
        setup = test_setup()  # pylint:disable=unused-variable

        get_offers_1 = _get_offers()
        get_offers_2 = _get_offers()

        assert not id(get_offers_1[0]) == id(get_offers_2[0])

    def test__run_fetch_task__calls_scheduler_service_method__when_is_called(self, test_setup):
        setup = test_setup(fetch_service=True)
        fscheduler_service = setup.fscheduler_service

        app = AppService()
        app.run_fetch_task()

        assert fscheduler_service.called
        assert isinstance(fscheduler_service.call_args.args[0], typing.Callable)

    def test__run_notify_task__calls_scheduler_service_method__when_is_called(self, test_setup):
        setup = test_setup(process_service=True)
        pscheduler_service = setup.pscheduler_service

        app = AppService()
        app.run_notify_task()

        assert pscheduler_service.called
        assert isinstance(pscheduler_service.call_args.args[0], typing.Callable)
