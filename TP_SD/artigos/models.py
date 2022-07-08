from django.db import models

from datetime import date

class art(models.Model):
    titulo = models.CharField(verbose_name="título",max_length=200)
    subtitulo = models.CharField(verbose_name="subtítulo",max_length=200)
    pub_date = models.DateTimeField('data de publicação')
#Transformar autor em Objeto ID
#autor = models.CharField(verbose_name="autor",max_length=100)
    palavra_chave = models.CharField(verbose_name="palavra_chave", max_length=500)

    def __str__(self):
        return self.name

class usuario(models.Model):

    name = models.CharField(verbose_name="name",max_length=100)
    email = models.EmailField('email')
    funcao = models.CharField(verbose_name="função",max_length=100)

    def __str__(self):
        return self.name
