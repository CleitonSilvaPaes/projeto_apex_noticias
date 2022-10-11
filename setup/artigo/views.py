from webbrowser import get
from django.shortcuts import render, redirect
from portal.views import create_context_base
from .models import *

# Create your views here.
def get_artigo(request, id=None):
    template_artigo = 'artigo/artigo.html'

    context = create_context_base()

    if id != None:
        if Artigo.objects.filter(id=id).exists():
        # context['noticia'] = Artigo.objects.all().filter(ativo='True').get(id=id)
        # mas para evita de fazer uma nova requisição ao banco de dados e feita dessa maneira
        # context['noticia'] = context['noticias'].get(id=id)
            context['noticia'] = context['noticias'].get(id=id)

            return render(request, template_artigo, context)
    else: 
        context['noticia'] = None

        return render(request, template_artigo, context)

    return redirect('index')