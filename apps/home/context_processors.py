from .models import SiteSettings

def get_logo(request):
    settings = SiteSettings.objects.first()
    return {
        "logo":f'/{settings.logo}'
    }

def get_urls(request):
    settings = SiteSettings.objects.first()
    return {
        "facebook_url":settings.facebook_url,
        "whatsapp_number": settings.whatsapp_number
    }