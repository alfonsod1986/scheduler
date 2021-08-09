from datetime import datetime, timedelta
from .constants import MAX_MINUTES_PER_ACTIVITY, ENABLED, DISABLED, PENDING, OVERDUE, DONE, UTC_TZ

def is_activity_lasts_a_maximum_one_hour(start_date, end_date):
    diff = end_date - start_date
    return (diff.seconds / 60) <= MAX_MINUTES_PER_ACTIVITY


def get_custom_now(add_days):
    now = datetime.now()
    custom_now = now + timedelta(days=add_days)
    return custom_now.strftime("%Y-%m-%d")


def get_conditional_status(schedule, status):
    now = UTC_TZ.localize(datetime.now())

    if status == ENABLED and schedule >= now:
        return PENDING
    if status == ENABLED and schedule < now:
        return OVERDUE
    return DONE