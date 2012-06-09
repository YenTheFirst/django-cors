from django.http import HttpResponse
from django.conf import settings

class AllowOriginMiddleware(object):
    def process_request(self, request):
        if request.method == 'OPTIONS':
            return add_origin(HttpResponse())

    def process_response(self, request, response):
        origin = request.META.get('HTTP_ORIGIN')
        allowed_origins = settings.ALLOWED_CROSS_DOMAIN_ORIGINS
        if origin and allowed_origins:
            if origin in allowed_origins or allowed_origins == '*' or allowed_origins == origin:
                response['Access-Control-Allow-Origin'] = origin
                response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
                response['Access-Control-Allow-Headers'] = 'Content-Type'
        if settings.ALLOWED_CROSS_DOMAIN_CREDENTIALS:
            response['Access-Control-Allow-Credentials'] = 'true'
        return response
