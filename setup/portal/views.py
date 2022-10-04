from django.shortcuts import render, redirect
from .models import PortalInfor
from artigo.models import Artigo, Categoria

# Create your views here.

def create_context_base():
    info_portal = PortalInfor.objects.all().last()
    
    noticias = Artigo.objects.all().filter(ativo='True')

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
        'categoria_atual' : None,
        'popular_news' : noticias[:3],
        'noticias' : noticias,
    }

    return context

    

def index(request):

    context = create_context_base()

    return render(request, 'index/index.html', context)

def categoria(request, nome=None):

    context = create_context_base()

    if nome != None:
        '''
            # feito dessa maneita para evitar de faze uma nova consuta ao banco
            # o mesmo resultado pode ser obitido com 
            # context['categoria_atual'] = Artigo.objects.all().filter(ativo='True').filter(categoria=Categoria.objects.get(nome=nome))
        '''
        context['categoria_atual'] = context['noticias'].filter(categoria=Categoria.objects.get(nome=nome))
        context['nome_categoria'] = nome
        return render(request, 'artigo/categoria.html', context)


    return render(request, 'artigo/categoria.html', context)

