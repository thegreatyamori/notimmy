import typing

import time
import schedule

_DEFAULT_FETCH_TIME = 15
_DEFAULT_PROCESS_TIME = 30


class SchedulerService:
    @staticmethod
    def run_fetch_live_offers(
        function: typing.Callable,
        *args,
        **kwargs,
    ):
        every_time = (
            _DEFAULT_FETCH_TIME
            if not kwargs.get('every_time') else
            kwargs.get('every_time')
        )
        schedule.every(every_time).minutes.do(function, *args, **kwargs)

    @staticmethod
    def run_process_live_offers(
        function: typing.Callable,
        *args,
        **kwargs,
    ):
        every_time = (
            _DEFAULT_PROCESS_TIME
            if not kwargs.get('every_time') else
            kwargs.get('every_time')
        )
        schedule.every(every_time).minutes.do(function, *args, **kwargs)

    @staticmethod
    def execute_jobs():
        schedule.run_pending()
        time.sleep(1)


# def hello(name):
#     greeting = "Hola"
#     print(f"{greeting} {name}")
#     return f"{greeting} {name}"
#
#
# s = SchedulerService
#
#
# s.run_process_live_offers(hello, 'Jerson')
# s.run_fetch_live_offers(hello, 'Jeyssi')
# while True:
#     s.execute_jobs()
