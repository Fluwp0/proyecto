from django.shortcuts import render, get_object_or_404, redirect
from .models import Auto
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.http import JsonResponse



def modelos(request):
    autos = Auto.objects.all()
    return render(request, 'autos/modelos.html', {'autos': autos})

def index(request, id):
    auto = get_object_or_404(Auto, id=id)
    return render(request, 'autos/index.html', {'auto': auto})