__BEFORE_DJANGO_APPS = (  # Apps de terceros que deben cargar antes que las de Django

)

__DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',
    'django.contrib.gis'
)



__AFTER_DJANGO_APPS = (  # Apps de terceros que deben cargar después que las de Django
)

__OWN_APPS = (
    'scheduler.apps.apidoc',
    'scheduler.apps.security',
)

__THIRD_PARTY_APPS = (
    'rest_framework',
    'django_filters',
    'drf_yasg',
    'corsheaders',
    'django_extensions',
    
)

INSTALLED_APPS = __BEFORE_DJANGO_APPS + __DJANGO_APPS + __AFTER_DJANGO_APPS + __OWN_APPS + __THIRD_PARTY_APPS
