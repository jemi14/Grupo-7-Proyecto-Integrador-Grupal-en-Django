# Codo a Codo 2022

# Entrega grupo  7 : Griselda Benitez - Martín Estrada - Martín Guzmán - Matias Bergamaschi - Agustín Guarmes.

#Consignas y cumplimiento: 

• El proyecto debe encontrarse subido a un repositorio git en la nube con acceso a todos
los participantes y el docente (pude estar público). Pueden entrar desde: https://github.com/jemi14/Grupo-7-Proyecto-Integrador-Grupal-en-Django

• Deben existir al menos 3 rutas distintas. El proyecto tiene una unica APP con 4 modelados, en el archivo urls.py estan todas las rutas, alrededor de 15

• Debe existir al menos una vista parametrizada. Hay varias, por ejemplo los eliminar, son con vistas parametrizadas, aúnque tambien con vistas basadas en clases
• Deben utilizarse templates que cumplan con lo siguiente:

o Debe haber al menos un template asociado a una vista.
o Debe existir al menos una relación de herencia entre templates.
o Debe existir al menos un filtro aplicado.
o Debe existir al menos un template que utilice archivos estáticos (js, css, etc).

Todo esto se cumple ampliamente, todos heredan de padre.html, todos usan boostrap y js, en las listas se implemtan filtros. 


• Se deben utilizar Django Forms que cumplan con las siguientes características:
o Al menos un formulario debe poseer validaciones en el front-end y en el backend
o Debe haber al menos un formulario asociado a un template.
o Debe haber al menos un formulario basado en clases.
o Debe haber al menos un formulario asociado a un modelo

Usamos los formularios de django en form.py , el de medicos tiene doble validación. 



• Deben existir al menos dos modelos distintos que posean una relación de uno a muchos

Generamos una sola relación entre User (de django) y avatar. No nos parecio oportuno que sea uno a muchos, hicimos uno a uno, pero con imagen. 

• El proyecto debe funcionar utilizando un servidor de base de datos local dentro de los
soportados (en el curso se recomienda PostgreSQL), y debe poseer las migraciones
necesarias para su funcionamiento.

Esto está perfecto, igual no le pusimos semillas visibles a la BD, si quieren usar al 100% la app deberian crear un superusuario conocido
python manage.py createsuperuser



• Se debe poder acceder al admin de django y al menos un modelo debe poder
administrarse desde el admin.

Todos estan disponibles desde el panel para hacer crud.

• El proyecto debe poseer al menos una página a la que solo se pueda acceder mediante
un usuario autenticado y al misma debe validar tanto en el front-end como en el backend.

Solo se pueden eliminar medicos su estas autentificado, tambien no se puede agregar avatar si no estas logueado. 
