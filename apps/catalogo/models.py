from django.db import models

# Create your models here.

class Catalogo(models.Model):
    Existencia = (
    ('C', 'Con existencia'),
    ('S', 'Sin existencia'),
    )
    id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=40, blank=False, null=False)
    modelo = models.CharField(max_length=100, blank=False, null=False)
    años = models.CharField(max_length=100, blank=False, null=False)
    posicion = models.CharField(max_length=200, blank=False, null=False)
    dimensionx = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=False)
    dimensiony = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=False)
    dimensionz = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=False)
    imagen = models.ImageField(upload_to='catalog/', max_length=200, blank=False, null=False)
    existencia = models.CharField(blank=True, max_length=1, choices=Existencia)

    class Meta:
        verbose_name = 'Catalogo'
        verbose_name_plural = 'Catalogos'
        ordering = ['marca']

    def __str__(self):
        return self.marca
