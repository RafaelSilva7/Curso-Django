# forms.py

from django import forms

from .models import Assunto, Entrada


class AssuntoForm(forms.ModelForm):
    """Formulário para o modelo assunto"""
    
    class Meta:
        model = Assunto
        fields = ['titulo']


class EntradaForm(forms.ModelForm):
    """Formulário para o modelo entrada"""
    
    class Meta:
        model = Entrada
        fields = ['titulo', 'texto', 'imagem']
