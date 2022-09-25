from django.contrib import admin
from .models import Autor, Artigo, Categoria, ControleViews

admin.site.site_header = 'Portal de Noticias'

# Start Admin Autor
class ListandoAutor(admin.ModelAdmin):

    list_display = ('id', 'nome', 'avatar', 'apresentacao')
    list_display_links = ('id', 'nome', 'apresentacao')
    search_fields = ('id', 'nome')

admin.site.register(Autor, ListandoAutor)
# End Admin Autor

# Start Admin Artigo
class ListandoArtigo(admin.ModelAdmin):

    list_display = ('id', 'titulo', 'autor', 'categoria', )
    list_display_links = ('id', 'autor', 'categoria')
    search_fields = ('id', 'autor', 'titulo')

admin.site.register(Artigo, ListandoArtigo)
# End Admin Artigo

# Start Admin Categoria
class ListandoCategoria(admin.ModelAdmin):

    list_display = ('id', 'nome', )
    list_display_links = ('id', 'nome')
    search_fields = ('id', 'nome')

admin.site.register(Categoria, ListandoCategoria)
# End Admin Categoria

class ListandoControleViews(admin.ModelAdmin):

    list_display = ('id', 'artigo_id', )
    list_display_links = ('id', 'artigo_id')
    search_fields = ('id', 'artigo_id')

admin.site.register(ControleViews, ListandoControleViews)