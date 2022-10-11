from django.shortcuts import render, redirect
from portal.views import create_context_base
from .forms import ComentarioForm
from .models import *

# Create your views here.
def get_artigo(request, id=None):
    template_artigo = 'artigo/artigo.html'

    context = create_context_base()
    context['comentarioForm'] = ComentarioForm

    if id != None:
        if Artigo.objects.filter(id=id).exists():
        # context['noticia'] = Artigo.objects.all().filter(ativo='True').get(id=id)
        # mas para evita de fazer uma nova requisição ao banco de dados e feita dessa maneira
        # context['noticia'] = context['noticias'].get(id=id)
            context['noticia'] = context['noticias'].get(id=id)
            comentarios_list = context['noticia'].comentarios.filter(ativo=True)
            context['comentarios'] = comentarios_list

            return render(request, template_artigo, context)
    else: 
        context['noticia'] = None

        return render(request, template_artigo, context)

    return redirect('index')
    
def add_comentario(request, id):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        print(f" =================================== {request.POST}")
        if form.is_valid():
            novo_comentario = form.save(commit=False)
            novo_comentario.artigo = Artigo.objects.get(id=id)
            novo_comentario.save()

    return redirect('artigo', id=id)