# Definine os padrões de URL para o módulo de usuários
from django.conf.urls import url

from . import views

app_name="users"

urlpatterns = [
    # Página de registro
    url(r'^registro/$', views.RegistroView.as_view(), name='registro'),
    
    # Página de login
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    
    # Página de logout
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
]
