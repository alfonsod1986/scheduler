from django.urls import path, include

app_name = 'schedule'

urlpatterns = [
    path('api/', include('scheduler.apps.schedule.api.urls')),
]

