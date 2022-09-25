from django.db import models

# Create your models here.
class PortalInfor(models.Model):
    titlo_portal = models.CharField(max_length=60, default='Apex')
    email = models.CharField(max_length=200, blank=True)
    telefone = models.CharField(max_length=40, blank=True)
    endereco = models.CharField(max_length=255, blank=True)
    facebook = models.CharField(max_length=255, blank=True)
    youtube = models.CharField(max_length=255, blank=True)
    instagram = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
