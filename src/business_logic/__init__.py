from .services import AppService, SchedulerService


class Bot:
    def __init__(self, defaults):
        self.scheduler_service = SchedulerService(defaults.fetch_time, defaults.process_time)
        self.app_service = AppService(defaults=defaults)

    def _run_fetch_task(self):
        self.scheduler_service.run_fetch_live_offers(self.app_service.fetch_and_save)

    def _run_notify_task(self):
        self.scheduler_service.run_process_live_offers(self.app_service.process_and_notify)

    def run_tasks(self):
        self._run_fetch_task()
        self._run_notify_task()
