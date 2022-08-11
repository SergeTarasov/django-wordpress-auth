from django.utils.functional import SimpleLazyObject

from .utils import get_wordpress_user


class WordPressAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.wordpress_user = SimpleLazyObject(lambda: get_wordpress_user(request))
        return self.get_response(request)
