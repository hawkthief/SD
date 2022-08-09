from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import newuserForm

@login_required()
def home(request):
    return redirect('/artigos/search')

@login_required()
def manageusers(request):
    if request.user.is_superuser:

        return render(request, 'users.html')
    else:
        return redirect('/artigos/search/')

def newuser(request):
    if request.method == 'POST':
        form = newuserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
        return redirect('/artigos/search/')
    else:
        form = newuserForm()
    return render(request, 'register.html', {'form': form})
