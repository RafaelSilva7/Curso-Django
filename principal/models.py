from django.db import models
from django.contrib.auth.models import User


def imagem_entrada(instance, filename):
    """Configurações para o salvamento de imagens"""
    path = str(instance.usuario.username).lower().replace(' ', '_')
    return '{username}/{file}'.format(username=path, file=filename)


class Assunto(models.Model):
    """Um assunto para as entradas postadas"""
    titulo = models.CharField(max_length=200, verbose_name='Título')
    data_adicao = models.DateField(auto_now_add=True, verbose_name='Data de adição')
    
    def __str__(self):
        """Devolve uma representação do modelo"""
        return self.titulo


class Entrada(models.Model):
    """Uma entrada para o blog"""
    usuario = models.ForeignKey(User, on_delete='cascade')
    assunto = models.ForeignKey(Assunto, on_delete='cascade')
    imagem = models.TextField(blank=True, null=True, verbose_name='Imagem')
    titulo = models.CharField(blank=True, null=True, max_length=200, verbose_name='Título')
    texto = models.TextField(blank=True, null=True, verbose_name='Texto')
    data_adicao = models.DateField(auto_now_add=True, verbose_name='Data de adição')
    
    def __str__(self):
        """Devolve uma representação do modelo"""
        return self.texto[:50] + '...'
    
