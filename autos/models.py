from django.db import models

class Auto(models.Model):
    modelo = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=15, decimal_places=0)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='autos/')
    
    def __str__(self):
        return self.modelo
