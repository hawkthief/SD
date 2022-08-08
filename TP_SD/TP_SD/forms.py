from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from artigos.models import *


class newuserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = usuario
        fields = ("name", "username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(newuserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
