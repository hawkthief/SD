from django import forms
from django.db import models
from .models import *


class artForm(forms.ModelForm):
    class Meta:
        model = art
        fields = '__all__'
        exclude = ['author']


class searchForm(forms.ModelForm):
    class Meta:
        model = art
        fields = '__all__'
        exclude = ['file']
        #widgets = {
        #    'pub_date': DateInput(),
        #}

class nuserForm(forms.ModelForm):
    class Meta:
        model = usuario
        fields = '__all__'
