from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import newuserForm
from artigos.forms import searchForm
from artigos.models import *
import pandas as pd

@login_required()
def home(request):
    if request.method == 'POST':
        form = searchForm(request.POST)
        if form.is_valid():
            pass
        return redirect('/artigos/')
    else:
        form = searchForm()
    return render(request, 'index.html', {'form': form})

@login_required()
def manageusers(request):
    if request.user.is_superuser:

        return render(request, 'users.html')
    else:
        return render(request, 'index.html')

def newuser(request):
    if request.method == 'POST':
        form = newuserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
        return redirect('/')
    else:
        form = newuserForm()
    return render(request, 'register.html', {'form': form})
