from .json_reader import json_settings

settings = json_settings()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': settings["DB"]["HOST"],
        'NAME': settings["DB"]["NAME"],
        'USER': settings["DB"]["USER"],
        'PASSWORD': settings["DB"]["PASSWORD"],
        'PORT': settings["DB"]["PORT"],
    }
}
