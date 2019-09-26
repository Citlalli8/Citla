from django.shortcuts import render

# Create your views here.

def index(request):
     return render(request, 'index.html', {'autos': autos})

class Auto:
    def __init__(self, nombre, precio, modelo, color):
        self.nombre = nombre
        self.precio = precio 
        self.modelo = modelo 
        self.color = color


autos = [
    Auto('Jetta',145000, 2018,"Gris"),
    Auto('Camaro', 600000, 2019, ' Negro'),
    Auto('Audi 7', 90000, 2018, 'blanco'),
    Auto('Futura', 900000, 1954, 'Aqua'),
]
