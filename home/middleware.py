# home/middleware.py
from django.utils import translation
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

class ExcludeAdminLocaleMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Check if the request path is for the admin panel
        if request.path.startswith(reverse('admin:index')):
            # Deactivate translation for the admin panel
            translation.deactivate()
        else:
            # Activate translation for non-admin URLs
            # Use the default language code if not set
            lang_code = translation.get_language_from_request(request)
            translation.activate(lang_code)
            request.LANGUAGE_CODE = lang_code
