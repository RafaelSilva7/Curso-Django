"""Define os padrões de URL para a API REST"""

from django.conf.urls import url

from . import views

app_name="api"

urlpatterns = [
    # Retorn o token do usuário
    url(r'^token/$', views.AutenticacaoAPIView.as_view(), name='token'),

    # Retorna a lista com todos os assuntos
    url(r'^assuntos/$', views.AssuntosAPIView.as_view(), name='assuntos'),

    # Retorna a lista das entradas associadas ao usuário
    url(r'^entradas/(?P<usuario_id>\d+)/$', views.EntradasAPIView.as_view(), name='entradas'),

    # Edita uma entrada do usuário
    url(r'edita_entrada/(?P<pk>\d+)/$', views.EditaEntradaAPIView.as_view(), name='edita_entrada'),
]
