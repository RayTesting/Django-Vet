from .models import SiteSettings

def get_logo(request):
    settings = SiteSettings.objects.first()
    return {
        "logo":f'/{settings.logo}'
    }