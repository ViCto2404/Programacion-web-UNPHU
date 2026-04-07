from django.contrib import admin
from .models import Articulo, Noticia

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock')

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_publicacion')
    search_fields = ('titulo', 'resumen')
