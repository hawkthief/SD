from django import forms
from django.db import models
from .models import *


class artForm(forms.ModelForm):
    class Meta:
        model = art
        fields = '__all__'
        exclude = ['author']


class searchForm(forms.Form):

    title = forms.CharField(required=False)
    subtitle = forms.CharField(required=False)
    pub_date = forms.DateTimeField(required=False)
    author = forms.CharField(required=False)
    publisher = forms.CharField(required=False)
    keywords = forms.CharField(required=False)

class nuserForm(forms.ModelForm):
    class Meta:
        model = usuario
        fields = '__all__'
