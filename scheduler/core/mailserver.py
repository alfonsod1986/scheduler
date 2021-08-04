from ..core.json_reader import json_settings

settings = json_settings()

EMAIL_USE_TLS = settings["EMAIL"]["EMAIL_USE_TLS"]
EMAIL_HOST = settings["EMAIL"]["EMAIL_HOST"]
EMAIL_PORT = settings["EMAIL"]["EMAIL_PORT"]
EMAIL_HOST_USER = settings["EMAIL"]["EMAIL_HOST_USER"]
EMAIL_HOST_PASSWORD = settings["EMAIL"]["EMAIL_HOST_PASSWORD"]
DEFAULT_FROM_EMAIL = settings["EMAIL"]["DEFAULT_FROM_EMAIL"]
EMAIL_BACKEND = settings["EMAIL"]["EMAIL_BACKEND"]
EMAIL_USE_SSL = settings["EMAIL"]["EMAIL_USE_SSL"]


# For django mailer

MAILER_EMAIL_MAX_BATCH = settings["EMAIL"]["MAILER_EMAIL_MAX_BATCH"]
MAILER_EMAIL_THROTTLE = settings["EMAIL"]["MAILER_EMAIL_THROTTLE"]
