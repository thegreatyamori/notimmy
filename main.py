import logging

# from src.business_logic import AppService
#
#
# if __name__ == "__main__":
#     app = AppService()
#     app.run_fetch_task()
#     app.run_notify_task()
#     logging.info("Init bot...")
#     while True:
#         app.scheduler_service.execute_jobs()
from src.cli import app

if __name__ == "__main__":
    app()
