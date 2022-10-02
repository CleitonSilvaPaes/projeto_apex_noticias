from django.shortcuts import render, redirect
from portal.views import create_context_base
from .models import *

# Create your views here.
def get_artigo(request, id):

    context = create_context_base()

    if Artigo.objects.filter(id=id).exists():
        context['noticia'] = Artigo.objects.get(id=id)

        return render(request, 'artigo/artigo.html', context)

    return redirect('index')

    