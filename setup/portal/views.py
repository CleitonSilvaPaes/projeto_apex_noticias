from django.shortcuts import render
from .models import PortalInfor

# Create your views here.
def index(request):

    info_portal = PortalInfor.objects.all().last()

    context = {
        'titulo' : info_portal.titlo_portal,
        'contato': {
            'telefone': info_portal.telefone,
            'email' : info_portal.email,
            'endereco': info_portal.endereco,
        },
        'media_sociais': {
            'facebook': info_portal.facebook,
            'youtube' : info_portal.youtube,
            'instagram' : info_portal.instagram
        }
    }

    return render(request, 'index/index.html', context)