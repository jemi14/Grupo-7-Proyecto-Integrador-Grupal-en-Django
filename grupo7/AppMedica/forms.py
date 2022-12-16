from django import forms
from django.db.models.fields import DateField
from django.forms.fields import EmailField, IntegerField,CharField
import datetime

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MedicoFormulario(forms.Form):
    
    apellido = forms.CharField(max_length=40)
    especialidad = forms.CharField(max_length=40)
    matricula = forms.IntegerField()
    email = forms.EmailField()
    
class PacienteFormulario(forms.Form):
    
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    fNac=forms.DateField(initial=datetime.date.today)
    telefono=forms.IntegerField()
    email=forms.EmailField()
    servicio=forms.CharField(max_length=40)
    
class ContactoFormulario(forms.Form):
    
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    email=forms.EmailField()
    tel=forms.IntegerField()
    mensaje=forms.CharField(max_length=250)
    
    
class UserEditForm(UserCreationForm):

    #Obligatorios
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña')
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
    last_name = forms.CharField()
    first_name = forms.CharField()

  
 
    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2', 'last_name', 'first_name']


class UserRegisterForm(UserCreationForm):

    #Obligatorios
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
    
    #Extra
    last_name = forms.CharField()
    first_name = forms.CharField()
    imagen = forms.ImageField(required=False)
   
        
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']
        

class AvatarFormulario(forms.Form):

    
    imagen = forms.ImageField(required=False)
    
