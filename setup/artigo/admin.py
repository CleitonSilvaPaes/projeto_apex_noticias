from django.contrib import admin
from .models import Autor, Artigo, Categoria, ControleViews, Comentario

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

    list_display = ('id', 'titulo', 'autor', 'categoria', 'created_at', 'ativo')
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

# Start Admin Controle Views
class ListandoControleViews(admin.ModelAdmin):

    list_display = ('id', 'artigo_id', )
    list_display_links = ('id', 'artigo_id')
    search_fields = ('id', 'artigo_id')

admin.site.register(ControleViews, ListandoControleViews)
# End Admin Controle Views

# Start Admin Comentario
@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'mensagem', 'artigo', 'created_on', 'ativo')
    list_filter = ('ativo', 'created_on')
    search_fields = ('nome', 'email', 'mensagem')
    actions = ['aprovar_comentario', 'reprovar_comentario']

    def aprovar_comentario(self, request, queryset):
        queryset.update(ativo=True)

    def reprovar_comentario(self, request, queryset):
        queryset.update(ativo=False)
# End Admin Comentario