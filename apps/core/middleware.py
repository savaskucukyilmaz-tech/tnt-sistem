from django.utils import translation

class UserLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        lang = None
        user = getattr(request, "user", None)
        if user and user.is_authenticated:
            profile = getattr(user, "profile", None)
            if profile and profile.preferred_language:
                lang = profile.preferred_language
        if not lang:
            # fallback to session/cookie handled by LocaleMiddleware
            return self.get_response(request)

        with translation.override(lang):
            response = self.get_response(request)
        return response
