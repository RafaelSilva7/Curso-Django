from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Assunto, Entrada
from .forms import AssuntoForm, EntradaForm


class LoginRequired(LoginRequiredMixin):
    """Configurações para autenticação"""
    login_url = '/contas/login/'
    redirect_field_name = 'next'


class IndexView(View):
    """Página inicial do site"""
    
    def get(self, request):
        return render(self.request, 'principal/index.html')


class AssuntosView(LoginRequired, View):
    """Mostra os assuntos cadastrados"""

    def get(self, request):
        assuntos = Assunto.objects.order_by('data_adicao') 
        context = {'assuntos': assuntos}
        return render(self.request, 'principal/assuntos.html',
            context)


class AssuntoView(LoginRequired, View):
    """Mostra as entradas de um assunto"""
    
    def get(self, request, assunto_id):
        assunto = Assunto.objects.get(id=assunto_id)
        entradas = assunto.entrada_set.filter(usuario=request.user).order_by('-data_adicao')
        context = {'assunto': assunto, 'entradas': entradas}
        return render(self.request, 'principal/assunto.html',
            context)
    
    
class NovoAssuntoView(LoginRequired, View):
    """Cria um novo assunto"""
    
    def get(self, request):
        form = AssuntoForm()
        context = {'form': form}
        return render(self.request, 'principal/novo_assunto.html',
            context)
    
    def post(self, request):
        form = AssuntoForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('principal:assuntos'))

class NovaEntradaView(LoginRequired, View):
    """Cria uma nova entrada"""
    
    def get(self, request, assunto_id):
        assunto = Assunto.objects.get(id=assunto_id)
        form = EntradaForm()
        context = {'form': form, 'assunto': assunto}
        return render(self.request, 'principal/nova_entrada.html',
            context)
    
    def post(self, request, assunto_id):
        assunto = Assunto.objects.get(id=assunto_id)
        form = EntradaForm(data=request.POST)
        if form.is_valid():
            nova_entrada = form.save(commit=False)
            nova_entrada.assunto = assunto
            nova_entrada.usuario = request.user
            nova_entrada.save()
        return HttpResponseRedirect(reverse('principal:assunto', args=[assunto_id]))


class EditaEntradaView(LoginRequired, View):
    """Edita uma entrada"""
    
    def get(self, request, entrada_id):
        entrada = Entrada.objects.get(id=entrada_id)
        assunto = entrada.assunto
        form = EntradaForm(instance=entrada)
        context = {
            'entrada': entrada,
            'assunto': assunto,
            'form': form
        }
        return render(self.request, 'principal/edita_entrada.html',
            context)
    
    def post(self, request, entrada_id):
        entrada = Entrada.objects.get(id=entrada_id)
        assunto = entrada.assunto
        form = EntradaForm(instance=entrada, data=request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('principal:assunto', args=[assunto.id]))
