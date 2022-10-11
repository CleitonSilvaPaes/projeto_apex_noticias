from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.get_artigo, name='artigo'),
    path('addcoment/<int:id>', views.add_comentario, name='comentarios'),
    path('', views.get_artigo, name='artigo')

]
