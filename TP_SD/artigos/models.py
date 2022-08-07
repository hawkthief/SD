from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

class art(models.Model):
    title = models.CharField(verbose_name="título",max_length=200)
    subtitle = models.CharField(verbose_name="subtítulo",max_length=200)
    pub_date = models.DateTimeField('data de publicação')
    author = models.ForeignKey('usuario', on_delete=models.CASCADE)
    publisher = models.CharField(verbose_name="publicante", max_length=200)
    keyword = models.CharField(verbose_name="palavra_chave", max_length=500)

    def __str__(self):
        return self.name


class usuario(AbstractUser):

    name = models.CharField(verbose_name="nome",max_length=100)
    email = models.EmailField('email')

    def __str__(self):
        return self.name
