# forms.py

from django import forms
from django.contrib.auth.models import User


class RegistroForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class LoginForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'password']
