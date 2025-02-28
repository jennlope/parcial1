from django.db import models

# Create your models here.
class Vuelo(models.Model):
    Nacional = 'Nacional'
    Internacional = 'Internacional'
    Tipos = [(Nacional,'Nacional'),(Internacional,'Internacional')]
    
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255) 
    tipo = models.CharField(max_length=13, choices=Tipos)
    precio = models.IntegerField()
    
    