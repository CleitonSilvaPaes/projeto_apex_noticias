from django.contrib import admin
from .models import PortalInfor

admin.site.site_header = 'Portal de Noticias'

class ListandoInfoPortal(admin.ModelAdmin):
    list_display = ('id', 'titlo_portal', 'created_at')
    list_display_links = ('id', 'titlo_portal')
    search_fields = ('id', )

admin.site.register(PortalInfor, ListandoInfoPortal)