# Definine os padrões de URL para o site principal
from django.conf.urls import url

from . import views

app_name="principal"

urlpatterns = [
    # Página inicial
    url(r'^$', views.IndexView.as_view(), name='index'),
    
    # Página que mostra todos os assuntos
    url(r'^assuntos/$', views.AssuntosView.as_view(), name='assuntos'),
    
    # Mostra as informações de um único assunto
    url(r'^assuntos/(?P<assunto_id>\d+)/$', views.AssuntoView.as_view(), name='assunto'),
    
    # Página para criação de novos assuntos
    url(r'^novo_assunto/$', views.NovoAssuntoView.as_view(), name='novo_assunto'),
    
    # Página para a criação de novas entradas
    url(r'^nova_entrada/(?P<assunto_id>\d+)/$', views.NovaEntradaView.as_view(), name='nova_entrada'),
    
    # Página para a edição de entradas
    url(r'^edita_entrada/(?P<entrada_id>\d+)/$', views.EditaEntradaView.as_view(), name='edita_entrada')
]
