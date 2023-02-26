from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

"""Configurações das rotas do projeto"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # rota para arquivos de mídia
