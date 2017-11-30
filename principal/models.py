from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profesor(models.Model):
    usuario = models.ForeignKey(User)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=150)
    universidad = models.CharField(max_length=250)
    departamento = models.CharField(max_length=150)

    def __unicode__(self):
        return self.nombre

class Alumno(models.Model):
    usuario = models.ForeignKey(User)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=150)
    universidad = models.CharField(max_length=250)
    titulacion = models.CharField(max_length=250)
    
    def __unicode__(self):
        return self.nombre

class TFG(models.Model):
    titulo = models.CharField(max_length=150)
    titulacion = models.CharField(max_length=250)
    descripcion = models.TextField(verbose_name='Descripcion')
    profesor = models.ForeignKey(Profesor)
    alumno = models.ForeignKey(Alumno, blank=True, null=True)
