from django.db import models

class Autor(models.Model):

    nome = models.CharField(max_length=255, blank=False)
    avatar = models.CharField(max_length=300, default='https://www.gravatar.com/avatar/?s=200&r=pg&d=mp')
    apresentacao = models.TextField(blank=False)

class Categoria(models.Model):

    nome = models.CharField(max_length=100, blank=False)

class Artigo(models.Model):

    titulo = models.CharField(max_length=100, blank=False)
    subtitulo = models.CharField(max_length=100, blank=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    texto_destaque_1 = models.TextField(blank=True)
    texto_destaque_2 = models.TextField(blank=True)
    texto = models.TextField()
    img_url = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True, editable=True)

class ControleViews(models.Model):
    artigo_id = models.ForeignKey(Artigo, on_delete=models.CASCADE)
    clicks = models.IntegerField()