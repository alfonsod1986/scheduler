from django.urls import path
from scheduler.apps.security.api.api import user_api_view, user_detail_api_view

app_name = 'api'

urlpatterns = [
    path('users/', user_api_view, name='users_api'),
    path('users/<int:pk>/', user_detail_api_view, name='users_detail_api'),
]