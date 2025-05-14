from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .models import *

# Create your views here.
def Homepage(request):
    context = {}
    dados_home = homepage.objects.all()
    context['dados_home'] = dados_home
    return render(request, 'homepage.html', context)

def Login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
            return render(request, 'Login.html')

    else:
        return render(request, 'Login.html')

def Sair(request):
    logout(request)
    return redirect ('homepage')