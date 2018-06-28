from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .serializers import AssuntoSerializer, EntradaSerializer
from principal.models import Assunto, Entrada


class AutenticacaoAPIView(ObtainAuthToken):
    """Retorna o token do usuário"""
    
    def post(self, request, *args, **kwargs):
        response = {
            'sucesso': False,
            'mensagem': ''
        }
        authentication = super(AutenticacaoAPIView, self).post(request, *args, **kwargs)
        
        if authentication.status_code == status.HTTP_200_OK:
            token = Token.objects.get(key=authentication.data['token'])
            user = token.user
            
            response.update(token=token.key)
            response.update(mensagem="Usuário autenticado")
            response.update(sucesso=True)
            response.update(id=user.id)

        return Response(response)


class AssuntosAPIView(generics.ListCreateAPIView):
    """Retorna a lista com todos os assuntos ou cria um novo assunto"""
    permissions_classes = [permissions.AllowAny]
    queryset = Assunto.objects.all()
    serializer_class = AssuntoSerializer


class EntradasAPIView(generics.ListCreateAPIView):
    """Retorna a lista com todas as entradas ou cria uma nova"""
    permissions_classes = [permissions.IsAuthenticated]
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerializer

class EditaEntradaAPIView(generics.UpdateAPIView):
    """Edita uma entrada do usuario"""
    permissions_classes = [permissions.IsAuthenticated]
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerializer