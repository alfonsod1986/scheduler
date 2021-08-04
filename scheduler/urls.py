from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from .starter import Starter
from django.conf.urls.static import static
from scheduler.apps.apidoc.config import schema_view

admin.autodiscover()
urlpatterns = [
    path('', Starter.as_view(), name="starter"),
    path('', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    # Api apps
    path('api/doc/(?P<format>\.json|\.yaml)/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # Own Django Apps.
    path('security/', include('scheduler.apps.security.urls')),
    path('schedule/', include('scheduler.apps.schedule.urls')),
]

