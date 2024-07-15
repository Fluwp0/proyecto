from django.shortcuts import render, get_object_or_404, redirect
from .models import Auto
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.http import JsonResponse



def modelos(request):
    autos = Auto.objects.all()
    return render(request, 'autos/modelos.html', {'autos': autos})

