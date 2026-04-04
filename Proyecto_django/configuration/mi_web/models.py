from django.db import models

class Articulo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen_url = models.URLField(max_length=500, blank=True, null=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre
