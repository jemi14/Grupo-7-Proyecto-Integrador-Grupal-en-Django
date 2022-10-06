from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, "juegosApp/index.html")

def nosotros(request):
    lista = []
    lista.append({"nombre": "Matias Bergamaschi", "comentarios": "BLABLABLA"})
    lista.append({"nombre": "Martín Estrada", "comentarios": "BLABLABLA"})
    lista.append({"nombre": "Martin Guzmán", "comentarios": "BLABLABLA"})
    lista.append({"nombre": "Lucas Andrada", "comentarios": "BLABLABLA"})
    lista.append({"nombre": "Griselda Benitez", "comentarios": "BLABLABLA"})

    return render(request, "juegosApp/nosotros.html", {"lista_personas": lista})

def juegos(request):
    return render(request, "juegosApp/juegos.html")

