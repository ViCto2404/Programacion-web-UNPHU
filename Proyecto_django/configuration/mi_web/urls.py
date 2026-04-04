from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articulos/', views.articulos, name='articulos'),
    path('bulbasaur/', views.bulbasaur, name='bulbasaur'),
    path('charmander/', views.charmander, name='charmander'),
    path('squirtle/', views.squirtle, name='squirtle'),
    path('noticias/', views.noticias, name='noticias'),
    path('enlaces/', views.enlaces, name='enlaces'),
    path('contacto/', views.contacto, name='contacto'),
    path('privacidad/', views.privacidad, name='privacidad'),
]
