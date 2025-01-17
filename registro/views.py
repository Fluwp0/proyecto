from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistroForm
from django.contrib.auth import logout

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('autos') 
        else:
            return render(request, 'registro/sesion.html', {'error': 'Invalid credentials'})
    return render(request, 'registro/sesion.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('autos')
    else:
        form = RegistroForm()
    return render(request, 'registro/registrar.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('autos')
