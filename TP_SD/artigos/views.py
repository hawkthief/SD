from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from .forms import artForm
from .models import *

@login_required()
def index(request):
    return render(request, 'index.html')
@login_required()
def uploadpage(request):
    if request.method == 'POST':
        form = artForm(request.POST)
        nart = art()
        nart.title = form.data['title']
        nart.subtitle = form.data['subtitle']
        nart.pub_date = form.data['pub_date']
        nart.publisher = form.data['publisher']
        nart.keyword = form.data['keyword']
        nart.author = request.user
        nart.article = request.FILES.get('article')
        nart.save()
        return render(request, 'index.html')
    else:
        form = artForm()
    return render(request, 'upload.html', {'form': form})

