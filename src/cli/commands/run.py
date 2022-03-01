import logging

from src.business_logic import AppService


def run(defaults: object):
    is_running = False
    import typer
    typer.echo(defaults.trade)
    typer.echo(defaults.country)
    typer.echo(defaults.set_fetch_time)
    typer.echo(defaults.set_process_time)
    logging.info("running bot...")
    # app = AppService()
    # app.run_fetch_task()
    # app.run_notify_task()
    # while is_running:
    #     app.scheduler_service.execute_jobs()
