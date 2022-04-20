import src.business_logic as logic
import src.cli.defaults as default_params


def run(defaults: default_params.Defaults):
    app = logic.Bot(defaults=defaults)
    app.run_tasks()

    while defaults.is_running:
        app.scheduler_service.execute_jobs()
