from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import newuserForm
from artigos import APIs
from artigos.models import usuario
import pandas as pd

@login_required()
def home(request):
    return redirect('/artigos/search')

@login_required()
def manageusers(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            pass
        else:
            users = usuario.objects.all().values()
            df = pd.DataFrame(users)
            df = df[['name', 'email', 'is_superuser']]
            info = df.__array__()
            return render(request, 'users.html', {"info": info})

    else:
        return redirect('/artigos/search/')

def newuser(request):
    if request.method == 'POST':
        form = newuserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            if request.user == user:
                APIs.sendmail(user.email)
        return redirect('/artigos/search/')
    else:
        form = newuserForm()
    return render(request, 'register.html', {'form': form})
