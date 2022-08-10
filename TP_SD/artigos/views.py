from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from .forms import artForm
from .models import art, usuario
from .forms import searchForm
import mimetypes
import pandas as pd



def download_file(request, id):

    article = None
    try:
        article = art.objects.get(id=id)
    except:
        pass

    obj = article.article
    mime_type, _ = mimetypes.guess_type(obj.path)

    response = HttpResponse(obj, content_type=mime_type, )
    response['Content-Disposition'] = "attachment; filename=%s" % obj.name
    return response

@login_required()
def index(request):
    form = searchForm()
    if request.method == 'POST':
        articles = art.objects.all().values()
        authors = usuario.objects.all().values()
        if articles and authors:
            df = pd.DataFrame(authors)
            df.rename(columns={'id':'author_id'})
            newdf = pd.DataFrame(articles)
            artdf = pd.merge(newdf,df, left_on='author_id', right_on='id')
            search = searchForm(request.POST)
            artdf = artdf.astype({"pub_date": str})
            key = search.data['keywords'].split(',')
            precondition = '.str.contains("'
            postcondition = '")'
            keysearch = ""
            if len(key) == 1:
                keysearch = keysearch + 'keyword' + precondition + key[0] + postcondition
            else:
                for x in key:
                    keysearch = keysearch + 'keyword' + precondition + x +postcondition + " or "
                keysearch = keysearch + 'keyword' + precondition + key[0] + postcondition

            if search.data['author']:
                artdf = artdf.query('name'+precondition+search.data['author']+postcondition, engine='python')
            if search.data['title']:
                artdf = artdf.query('title'+precondition+search.data['title']+postcondition, engine='python')
            if search.data['subtitle']:
                artdf = artdf.query('subtitle'+precondition+search.data['subtitle']+postcondition, engine='python')
            if search.data['publisher']:
                artdf = artdf.query('publisher'+precondition+search.data['publisher']+postcondition, engine='python')
            if search.data['pub_date']:
                artdf = artdf.query('pub_date'+precondition+search.data['pub_date']+postcondition, engine='python')
            if search.data['keywords']:
                artdf = artdf.query(keysearch, engine='python')

            artdf[['new_date','split']] = artdf['pub_date'].str.split(' ', 1, expand=True)

            artdf = artdf[["id_x","author_id","name","title","subtitle","new_date","publisher","keyword"]]

            info = artdf.__array__()

            context = {
                'form': form,
                'articles': info
            }

            return render(request, 'index.html', context)

    return render(request, 'index.html', {'form': form})
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
        return redirect('/artigos/search/')
    else:
        form = artForm()
    return render(request, 'upload.html', {'form': form})

