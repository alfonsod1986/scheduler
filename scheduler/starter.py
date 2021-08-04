from django.views.generic import View
from django.http import JsonResponse
from scheduler.settings import json_settings

settings = json_settings()


class Starter(View):
    """
    Esta vista sirve solamente para consultar si el servicio se encuentra activo.
    """

    def get(self, request):
        #server_port = request.environ.get('SERVER_PORT', None)
        json_object = {'info': "API Service Ready",
                       'api-documentation': f"{settings['URL_SERVER']}/api/doc/"}
        return JsonResponse(json_object)
