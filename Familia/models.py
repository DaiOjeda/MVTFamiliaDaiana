from django.db import models

# Create your models here.
class Familia(models.Model):
    nombre = models.CharField(max_length=30)
    creacion = models.DateField()

class Hermano(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()

class Sobrino(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()

class Sobrina(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()

class Mascota(models.Model):
    nombre = models.CharField(max_length=30)
    comidaFav = models.CharField(max_length=30)

