from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required()
def index(request):
    return render(request, 'index.html')
@login_required()
def uploadpage(request):
    return render(request, 'upload.html')