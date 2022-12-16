from django.urls import path
from AppMedica import views,forms

#PARA EL LOGOUT
from django.contrib.auth.views import LogoutView


urlpatterns = [
    
    path('inicio/', views.inicio, name='Inicio'),
    path('servicios/', views.servicios, name='Servicios'),
    path('pacientes/', views.pacientes, name='Pacientes'),
    path('medicos/', views.medicos, name='Medicos'),
    path('contacto/', views.contacto, name='Contacto'),
    path('medicoFormulario/',views.medicoFormulario,name="MedicoFormulario"),
    path('pacienteFormulario/',views.pacienteFormulario,name="PacienteFormulario"),
    path('contactoFormulario/',views.contactoFormulario,name='ContactoFormulario'),
    path('busquedaMedico', views.busquedaMedico,name='BusquedaMedico'),
    path('buscarMedico/', views.buscarMedico),
    path('busquedaPaciente', views.busquedaPaciente, name="BusquedaPaciente"),
    path('buscarPaciente/', views.buscarPaciente),
    path('about',views.about,name="About"),
    path('pages/',views.pages,name="Pages"),
    path('pagesMedicos/',views.pagesMedicos,name="PagesMedicos"),
    path('pagesPacientes/',views.pagesPacientes,name="PagesPacientes"),
    path('pagesContacto/',views.pagesContacto,name="PagesContacto"),
    
    
    
    
    #CRUD
    path('leerMedicos', views.leerMedicos, name='LeerMedicos'),
    path('eliminarMedicos/<matricula_para_borrar>/', views.eliminarMedicos, name="EliminarMedicos"),
    path('editarMedicos/<matricula_para_editar>/', views.editarMedicos, name="EditarMedicos"),
    
    
    
    
    path('login', views.login_request, name="Login"),
    path('register', views.register, name="Register"),
    
    path('logout', LogoutView.as_view(template_name='AppMedica/logout.html'), name="Logout"),
    
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    
    
    path('agregarAvatar', views.agregarAvatar, name="AgregarAvatar"),
    
    
    #PARA CLASES BASADAS EN VISTAS
    path('paciente/list', views.PacienteList.as_view(), name='List'),
    
    path(r'^(?P<pk>\d+)$', views.PacienteDetalle.as_view(), name='Detail'),
    
    path(r'^nuevo$', views.PacienteCreacion.as_view(), name='New'),
    
    path(r'^editar/(?P<pk>\d+)$', views.PacienteUpdate.as_view(), name='Edit'),
    
    path(r'^borrar/(?P<pk>\d+)$', views.PacienteDelete.as_view(), name='Delete'),
    
    
    
    
    
]
