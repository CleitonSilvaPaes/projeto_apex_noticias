from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('wp-admim-login/', admin.site.urls),
    path('', include('portal.urls')),
    path('artigo/', include('artigo.urls')),
]
