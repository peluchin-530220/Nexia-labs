from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),              # Tu página principal
    path('sobre/', views.sobre, name='sobre'),        # nexia-labs.onrender.com/sobre/
    path('contacto/', views.contacto, name='contacto'), # nexia-labs.onrender.com/contacto/
]