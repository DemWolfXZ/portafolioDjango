from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('portafolio/', views.portafolio, name='portafolio'),
    path('contacto/', views.contacto, name='contacto'),
]