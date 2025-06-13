from django.db import models
# Create your models here.

class Comuna(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    poblacion = models.IntegerField(null = True)
    tasa_de_vulnerabilidad = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fecha_fundacion = models.DateField(auto_now_add=True)
