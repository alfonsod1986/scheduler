from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="SCHEDULER API",
        default_version='v1',
        description="API version 1 for True Home",
        contact=openapi.Contact(email="alfonsod18@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
