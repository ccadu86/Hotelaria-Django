from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from .models import *
from .forms import *

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
            context = {
                "alerta" : "Usuário ou Senha Invalida"
            }
            return render(request, 'Login.html', context)

    else:
        return render(request, 'Login.html')
    

def addQuarto(request):
    if request.method == 'POST':
        form = quartoForms(request.POST, request.FILES)        
        if form.is_valid():
            form.save()
            return redirect('addQuarto')
    else:    
        form = quartoForms()
    
    context = {'form': form}
    return render(request, 'addQuartos.html', context)


def Sair(request):
    logout(request)
    return redirect ('homepage')