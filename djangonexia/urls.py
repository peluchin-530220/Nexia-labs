from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.static import serve
from django.urls import re_path

urlpatterns = [
    path('admin/', admin.site.urls),  # <-- CORREGIDO AQUÍ (Antes decía split)
    path('', include('tasks.urls')),  # Rutas de tu app
]

# Forzar a Django a servir los archivos estáticos en Render cuando DEBUG = False
if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]