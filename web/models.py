from django.db import models


# Create your models here.
class Carro(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=400)
    color = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="imagenes_carro")
    cantidad = models.IntegerField()
    precio = models.FloatField()
    visible = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
