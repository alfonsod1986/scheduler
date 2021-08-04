REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'scheduler.core.custom_pagination.CustomPageNumberPagination',
    'PAGE_SIZE': 1000,
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
}
