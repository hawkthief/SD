from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

def home(request):

    return redirect('/artigos/')
