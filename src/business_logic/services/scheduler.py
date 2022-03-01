import time
import typing

import schedule

DEFAULT_FETCH_TIME = 15
DEFAULT_PROCESS_TIME = 30


class SchedulerService:
    def __init__(self, fetch_time=DEFAULT_FETCH_TIME, process_time=DEFAULT_PROCESS_TIME):
        self.fetch_time = fetch_time
        self.process_time = process_time

    def run_fetch_live_offers(
            self,
            function: typing.Callable,
            *args,
            **kwargs,
    ):
        schedule.every(self.fetch_time).minutes.do(function, *args, **kwargs)

    def run_process_live_offers(
            self,
            function: typing.Callable,
            *args,
            **kwargs,
    ):
        schedule.every(self.process_time).minutes.do(function, *args, **kwargs)

    @staticmethod
    def execute_jobs():
        schedule.run_pending()
        time.sleep(1)
