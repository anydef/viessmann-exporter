import atexit
import os
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from flask import Flask
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware

from viessmann_exporter.collector import scrape_vicare

poling_interval = os.getenv("VIESSMANN_POLLING_INTERVAL", "180")


# Create a metric to track time spent and requests made.
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
        '/metrics': make_wsgi_app()
    })

    scheduler = BackgroundScheduler()
    scheduler.add_job(func=scrape_vicare, next_run_time=datetime.now(), trigger='interval', seconds=int("180"))
    scheduler.start()
    # Shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())

    return app
