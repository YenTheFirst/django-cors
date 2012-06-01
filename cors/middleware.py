from django.http import HttpResponse
from django.conf import settings

def add_origin(response):
    if settings.ALLOWED_CROSS_DOMAIN_ORIGINS:
        response['Access-Control-Allow-Origin'] = ' '.join(settings.ALLOWED_CROSS_DOMAIN_ORIGINS)
    return response

class AllowOriginMiddleware(object):
    def process_request(self, request):
        if request.method == 'OPTIONS':
            return add_origin(HttpResponse())

    def process_response(self, request, response):
        return add_origin(response)
