from django.utils.deprecation import MiddlewareMixin


# from django.core.cache import cache

class AuthUserMiddleware(MiddlewareMixin):
    def process_request(self, request):
        pass