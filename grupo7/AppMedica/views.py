from django.contrib.auth.password_validation import password_changed
from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from AppMedica.models import Medico,Paciente,Contacto,Avatar

from AppMedica.forms import MedicoFormulario,ContactoFormulario,PacienteFormulario, UserRegisterForm, UserEditForm, AvatarFormulario

from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


def contactoFormulario (request):
    
    
    if request.method == "POST":
        
        miFormulario = ContactoFormulario(request.POST)
        
        if miFormulario.is_valid():  
            
            informacion = miFormulario.cleaned_data
        
            contactoInsta = Contacto(nombre=informacion["nombre"], apellido=informacion["apellido"],email=informacion["email"],tel=informacion["tel"],mensaje=informacion["mensaje"])
            
            contactoInsta.save()  
            
            return render(request,'AppMedica/inicio.html') 
        
    else:
        
        miFormulario = ContactoFormulario()
    
    
    return render(request,'AppMedica/contactoFormulario.html',{"miFormulario":miFormulario})

def pacienteFormulario (request):
    
   
    if request.method == "POST":
        
        miFormulario = PacienteFormulario(request.POST)
        
        if miFormulario.is_valid():  
            
            informacion = miFormulario.cleaned_data
        
            pacienteInsta = Paciente(nombre=informacion["nombre"], apellido=informacion["apellido"],dni=informacion["dni"],fNac=informacion["fNac"], telefono=informacion["telefono"], email=informacion["email"], servicio=informacion["servicio"])
            
            pacienteInsta.save()  
            
            return render(request,'AppMedica/inicio.html') 
        
    else:
        
        miFormulario = PacienteFormulario()
    
 
    return render(request,'AppMedica/pacienteFormulario.html',{"miFormulario":miFormulario})

@login_required
def medicoFormulario (request):
   

    if request.method == "POST":
        
        miFormulario = MedicoFormulario(request.POST)
        
        if miFormulario.is_valid():  
            
            informacion = miFormulario.cleaned_data
        
            medicoInsta = Medico(apellido=informacion["apellido"], especialidad=informacion["especialidad"],matricula=informacion["matricula"],email=informacion["email"])
            
            medicoInsta.save()  
            
            return render(request,'AppMedica/inicio.html') 
        
    else:
        
        miFormulario = MedicoFormulario()
    
   
    return render(request,'AppMedica/medicoFormulario.html',{"miFormulario":miFormulario})


def inicio(request):
    
    diccionario = {}
    cantidadDeAvatares = 0
    
    if request.user.is_authenticated:
        avatar = Avatar.objects.filter( user = request.user.id)
        
        for a in avatar:
            cantidadDeAvatares = cantidadDeAvatares + 1
        
       
    
    #return HttpResponse("Esto es una prueba del inicio")

    return render(request,'AppMedica/inicio.html')


def servicios(request):

    return render(request,'AppMedica/servicios.html')


def pacientes(request):

    return render(request,'AppMedica/pacientes.html')


def medicos(request):

    return render(request,'AppMedica/medicos.html')



def contacto(request):

    return render(request,'AppMedica/contacto.html')




def busquedaMedico(request):
    
    return render(request,'AppMedica/busquedaMedico.html')



def buscarMedico(request):
    
    
    if request.GET["apellido"]:
        
        apellido = request.GET["apellido"]
        
        medicos = Medico.objects.filter(apellido__icontains=apellido)
    
        
        return render(request, "AppMedica/resultadoMedicos.html",{"medicos":medicos, "apellido":apellido})
         
         
    else: 
        
        respuesta = "Por favor enviar más información"     
    
    return HttpResponse(respuesta)


def leerMedicos(request):
    
    medicos = Medico.objects.all()
    
    dir = {'medicos':medicos}
    
    return render(request,"AppMedica/leerMedicos.html",dir)


@login_required
def eliminarMedicos(request, matricula_para_borrar):
    
    medicoAEliminar = Medico.objects.get(matricula=matricula_para_borrar)
    medicoAEliminar.delete()
    
    #Volver al menú
    medicos = Medico.objects.all()
    
    return render(request, 'AppMedica/leerMedicos.html', {'medicos': medicos})
    
    
@login_required  
def editarMedicos(request, matricula_para_editar):
    
    medico = Medico.objects.get(matricula=matricula_para_editar)

    if request.method == "POST":
        
        miFormulario = MedicoFormulario(request.POST)
        
        if miFormulario.is_valid():  
            
            informacion = miFormulario.cleaned_data
        
            medico.apellido=informacion["apellido"]
            medico.especialidad=informacion["especialidad"]
            medico.matricula=informacion["matricula"]
            medico.email=informacion["email"]
                
            
            medico.save()  
            
            return render(request,'AppMedica/inicio.html') 
        
    else:
        
        miFormulario = MedicoFormulario(initial={"apellido":medico.apellido,"especialidad":medico.especialidad,"matricula":medico.matricula,"email":medico.email})
    
   
    return render(request,'AppMedica/editarMedicos.html',{"miFormulario":miFormulario, "matricula_para_editar": matricula_para_editar})  
    


def busquedaPaciente(request):
    
    return render(request,'AppMedica/busquedaPaciente.html')



def buscarPaciente(request):
    
    
    if request.GET["apellido"]:
        
        apellido = request.GET["apellido"]
        
        pacientes = Paciente.objects.filter(apellido__icontains=apellido)
    
        
        return render(request, "AppMedica/resultadoPacientes.html",{"pacientes":pacientes, "apellido":apellido})
         
         
    else: 
        
        respuesta = "Por favor enviar más información"     
    
    return HttpResponse(respuesta)



def login_request(request):
    
    if request.method =="POST":
        
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            
            user = authenticate(username=usuario, password = contra)
            
            if user is not None:
                
                login(request, user)
                
                return render(request, "AppMedica/inicio.html", {"mensaje":f"BIENVENIDO a CHApp MEDICA, {usuario}!"})
                
            else:
                
                return render(request, "AppMedica/inicio.html", {"mensaje":f"LOS DATOS INGRESOS SON INCORRECTOS"})
                
            
        else:
            
            return render(request, "AppMedica/inicio.html", {"mensaje":f"FORMULARIO erroneo"})
            
            
    
    
    form = AuthenticationForm()  
    
    return render(request, "AppMedica/login.html", {"form":form} )



@csrf_exempt
def register(request):

      if request.method == 'POST':

            form = UserRegisterForm(request.POST)
            
            if form.is_valid():

                  username = form.cleaned_data['username']
                  
                                 
                  form.save()
                  
                  return render(request,"AppMedica/inicio.html" ,  {"mensaje":f"{username} Creado "})


      else:     
            miFormulario= AvatarFormulario() #Formulario vacio para construir el html
              
            form = UserRegisterForm()     

      return render(request,"AppMedica/register.html" ,  {"form":form})
             
  
@login_required
def editarPerfil(request):
    
    
    usuario = request.user
    
    if request.method == 'POST':
        
        miFormulario = UserEditForm(request.POST)
        
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
            
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.save()
            
            return render(request, "AppMedica/inicio.html")
        
    else:
        
        miFormulario = UserEditForm(initial={'email':usuario.email})
        
        
    return render(request, "AppMedica/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})


@login_required
def agregarAvatar(request):
      if request.method == 'POST':

            miFormulario = AvatarFormulario(request.POST, request.FILES) 

            if miFormulario.is_valid():   

                  u = User.objects.get(username=request.user)
                
                  avatar = Avatar (user=u, imagen=miFormulario.cleaned_data['imagen']) 
      
                  avatar.save()

                  return render(request, "AppMedica/inicio.html")

      else: 

            miFormulario= AvatarFormulario() #Formulario vacio para construir el html

      return render(request, "AppMedica/agregarAvatar.html", {"miFormulario":miFormulario})


 
def about(request):
    return render(request,'AppMedica/about.html')


def pages(request):
    return render(request,'AppMedica/pages.html')


def pagesMedicos(request):
    return render(request,'AppMedica/pagesMedicos.html')


def pagesPacientes(request):
    return render(request,'AppMedica/pagesPacientes.html')


def pagesContacto(request):
    return render(request,'AppMedica/pagesContacto.html')






#Leer --- nos da todos los cursos
class PacienteList(ListView):
    
    model = Paciente
    template_name = "AppMedica/paciente_list.html"
    
#Detalle - SUPER Leer - Buscar!!!!!
class PacienteDetalle(DetailView):
    
    model = Paciente
    template_name = "AppMedica/paciente_detalle.html"
    
#Crear elementos
class PacienteCreacion(CreateView):
    
    model = Paciente
    success_url = "../AppMedica/paciente/list"  #AppCoder/template/AppCoder/editar
    fields = ["nombre", "apellido", "fNac", "telefono", "email", "servicio"]
    
#modificar!!!!!!!!!!! 
class PacienteUpdate(UpdateView):
    
    model = Paciente
    success_url = "../paciente/list"
    fields = ["nombre", "apellido", "fNac", "telefono", "email", "servicio"]
  
#Borrar 
class PacienteDelete(DeleteView):
    
    model = Paciente
    success_url = "../paciente/list"