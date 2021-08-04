from django.urls import path, include

app_name = 'security'

urlpatterns = [
    path('api/', include('scheduler.apps.security.api.urls')),
]