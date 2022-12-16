from django.db import models
from django.db.models.fields import EmailField, IntegerField,CharField
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField

class Medico(models.Model):

    apellido = models.CharField(max_length=40)
    especialidad = models.CharField(max_length=40)
    matricula = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.apellido}, {self.especialidad}, {self.matricula},{self.email}"


class Paciente(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    fNac = models.DateField()
    telefono = models.IntegerField()
    email = models.EmailField(null=True)
    servicio = models.CharField(max_length=40, default='')
    
    
    def __str__(self):

        return f"{self.nombre}, {self.apellido}, {self.fNac}, {self.telefono}, {self.email}, {self.servicio}"


class Contacto(models.Model):
    
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField()
    tel=models.IntegerField()
    mensaje=models.CharField(max_length=250)
    
    def __str__(self):
        
        return f"{self.nombre},{self.apellido},{self.email},{self.tel},{self.mensaje}"
    
    
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatares',null=True,blank =True)
