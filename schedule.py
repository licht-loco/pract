import time
from datetime import datetime
from threading import Timer

from dailyVote import run_daily_vote
from discounts import run_weekly_discounts
from free import run_free_books
from novinki import run_novinki
from top25 import run_monthly_top25
from writersRec import run_writers_recommendations
LAST_RUN_TIME = {}
def interval_since_last_run(func_name):
    global LAST_RUN_TIME
    now = datetime.now()
    if func_name in LAST_RUN_TIME:
        delta = now - LAST_RUN_TIME[func_name]
        return delta.total_seconds()
    return float('inf') 
def run_every_day(func):
    """Запускается ежедневно"""
    global LAST_RUN_TIME
    seconds_in_a_day = 86400
    delay = max(seconds_in_a_day - interval_since_last_run(func.__name__), 0)
    timer = Timer(delay, lambda: _run_and_schedule(func))
    timer.start()
    LAST_RUN_TIME[func.__name__] = datetime.now()

def run_every_week(func):
    """Запускается еженедельно"""
    global LAST_RUN_TIME
    seconds_in_a_week = 604800
    delay = max(seconds_in_a_week - interval_since_last_run(func.__name__), 0)
    timer = Timer(delay, lambda: _run_and_schedule(func))
    timer.start()
    LAST_RUN_TIME[func.__name__] = datetime.now()

def run_every_month(func):
    """Запускается ежемесячно"""
    global LAST_RUN_TIME
    days_in_a_month = 30 * 24 * 3600 
    delay = max(days_in_a_month - interval_since_last_run(func.__name__), 0)
    timer = Timer(delay, lambda: _run_and_schedule(func))
    timer.start()
    LAST_RUN_TIME[func.__name__] = datetime.now()
def _run_and_schedule(func):
    func()
    if func.__name__.startswith('run'):
        if 'daily' in func.__name__:
            run_every_day(func)
        elif 'weekly' in func.__name__:
            run_every_week(func)
        elif 'monthly' in func.__name__:
            run_every_month(func)
if __name__ == '__main__':
    run_every_day(run_daily_vote)
    run_every_week(run_weekly_discounts)
    run_every_week(run_writers_recommendations)
    run_every_week(run_free_books)
    run_every_month(run_monthly_top25)
    run_every_week(run_novinki)
    while True:
        time.sleep(1)
