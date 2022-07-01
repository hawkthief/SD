from django.db import models

from django.db import models


class art(models.Model):
    titulo = models.CharField(verbose_name="título",max_length=200)
    pub_date = models.DateTimeField('date published')

