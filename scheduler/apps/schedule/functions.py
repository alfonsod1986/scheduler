from datetime import datetime
from .constants import MAX_MINUTES_PER_ACTIVITY

def is_activity_lasts_a_maximum_one_hour(start_date, end_date):
    diff = end_date - start_date
    return (diff.seconds / 60) <= MAX_MINUTES_PER_ACTIVITY