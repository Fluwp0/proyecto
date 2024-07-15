from django.shortcuts import render, get_object_or_404
from .models import Auto






def modelos(request):
    autos = Auto.objects.all()
    return render(request, 'autos/modelos.html', {'autos': autos})

def index(request, id):
    auto = get_object_or_404(Auto, id=id)
    return render(request, 'autos/index.html', {'auto': auto})