from pytz import timezone
from scheduler.core.internationalization import TIME_ZONE

ENABLED = 'Enabled'
DISABLED = 'Disabled'
LOCAL_TZ = timezone(TIME_ZONE)
UTC_TZ = timezone('UTC')
MAX_MINUTES_PER_ACTIVITY = 60
MAX_HOUR_PER_ACTIVITY = 1
PENDING = 'Pendiente a realizar'
OVERDUE = 'Atrasada'
DONE = 'Finalizada'

NOW_AFTER_TWO_WEEKS_ON_DAYS = 14
NOW_BEFORE_THREE_DAYS = -3