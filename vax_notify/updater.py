from apscheduler.schedulers.background import BackgroundScheduler
from .notify import notify
from datetime import datetime
import os

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(notify,'interval', minutes=45)
    scheduler.start()