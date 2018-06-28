from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistroForm, LoginForm


class RegistroView(View):
    """Página para o registro do usuário"""
    
    def get(self, request):
        form = RegistroForm()
        context = {'form': form}
        return render(self.request, 'users/registro.html', context)
    
    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        User.objects.create_user(username=username, email=email, password=password)
        usuario = authenticate(username=username, password=password)
        login(request, usuario)
        return HttpResponseRedirect(reverse('principal:index'))


class LoginView(View):
    """Página para a autenticação do usuário"""
    
    def get(self, request):
        form = LoginForm()
        context = {'form': form}
        return render(self.request, 'users/login.html', context)
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
        return HttpResponseRedirect(reverse('principal:index'))
    
class LogoutView(View):
    """Página para logout do usuário"""
    
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('principal:index'))
