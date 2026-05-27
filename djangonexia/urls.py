from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('sobre/', views.sobre, name='sobre'),
    path('admin/', admin.site.urls),
]