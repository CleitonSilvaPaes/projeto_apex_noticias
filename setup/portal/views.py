from django.shortcuts import render
from .models import PortalInfor
from artigo.models import Artigo, Categoria

# Create your views here.

def create_context_base():
    info_portal = PortalInfor.objects.all().last()
    noticias = Artigo.objects.all()
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
        },
        'lista_noticias' : noticias[:4],
        'categorias' : Categoria.objects.all(),
        'popular_news' : noticias[:3],
        'noticias' : noticias
    }

    return context

    

def index(request):

    context = create_context_base()

    return render(request, 'index/index.html', context)