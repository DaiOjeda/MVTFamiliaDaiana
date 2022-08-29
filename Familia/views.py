from django.shortcuts import render
from Familia.models import Familia, Hermano, Sobrina, Sobrino, Mascota
from datetime import datetime

# Create your views here.
def familia(request):
    miFamilia = Familia(nombre="Ojeda", creacion=datetime.now())
    miFamilia.save()
    contexto = {
        'familia': miFamilia
    }
    return render(request,'familia.html', contexto)

def hermano(request):
    miHermano = Hermano(nombre="Leo", edad=45)
    miHermano.save()
    contexto = {
        'hermano': miHermano
    }
    return render(request,'familia.html', contexto)

def sobrino(request):
    miSobrino = Sobrino(nombre="Valentino", edad=16)
    miSobrino.save()
    contexto = {
        'sobrino': miSobrino
    }
    return render(request,'familia.html', contexto)

def sobrina(request):
    miSobrina = Sobrina(nombre="Uma", edad=7)
    miSobrina.save()
    contexto = {
        'sobrina': miSobrina
    }
    return render(request,'familia.html', contexto)

def mascota(request):
    miMascota = Mascota(nombre="Saoko", comidaFav="Atún")
    miMascota.save()
    contexto = {
        'mascota': miMascota
    }
    return render(request, 'familia.html', contexto)



