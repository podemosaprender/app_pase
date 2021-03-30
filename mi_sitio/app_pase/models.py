from djgeojson.fields import PointField
from django.db import models


class Lugar(models.Model):

    nombre = models.CharField(max_length=256)
    descripcion = models.TextField()
    foto = models.ImageField()
    latlng = PointField()

    def __str__(self):
        return self.nombre

    @property 
    def foto_url(self):
        return self.foto.url