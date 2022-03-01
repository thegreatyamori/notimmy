from src.business_logic import Bot


def run(defaults: object):
    is_running = True

    app = Bot(defaults=defaults)
    app.run_tasks()

    while is_running:
        app.scheduler_service.execute_jobs()
