from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path

urlpatterns = [
    path('admin/', admin.site.split), # Revisa si tu ruta de admin se llama admin/ o tiene otro nombre
    path('', include('tasks.urls')),   # Las rutas de tu aplicación local
]

# FORZAR A DJANGO A SERVIR ESTÁTICOS EN PRODUCCIÓN (RENDER)
if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?H.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]
else:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = [
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('sobre/', views.sobre, name='sobre'),
    path('admin/', admin.site.urls),
]