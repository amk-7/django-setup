from django.conf import settings

def bootstrap(request):
    return {
        'is_user' : request.session.get('is_user'),
        'APP_NAME' : settings.APP_NAME,
        'MEDIA_URL' : '/media/',
    }

