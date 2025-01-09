from django.shortcuts import render
from .models import Autor, Libro

# Create your views here.
def index(request):
    autores = Autor.objects.all()
    libros = Libro.objects.all()
    context = {
        'autores': autores,
        'libros': libros
    }
    return render(request, 'modelos/index.html', context)
