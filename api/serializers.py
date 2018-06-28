from rest_framework import serializers

from principal.models import Assunto, Entrada


class AssuntoSerializer(serializers.ModelSerializer):
    """Serializer do modelo Assunto"""
    
    class Meta:
        model = Assunto
        fields = ('titulo',)


class EntradaSerializer(serializers.ModelSerializer):
    """Serializer do modelo de Entrada"""

    class Meta:
        model = Entrada
        exclude = ('data_adicao',)