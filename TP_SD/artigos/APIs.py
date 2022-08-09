from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .forms import artForm
from .models import art, usuario
from .forms import searchForm
import pandas as pd
import mimetypes
import os


class DeleteArt(APIView):
    def get(self, request):

        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        article = None
        try:
            article = art.objects.get(id=request.data['id'])
        except:
            pass
        if (request.user.is_superuser or request.user.id == article.author.id):
            if article:
                article.delete()
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class EditMeta(APIView):
    def get(self, request):

        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        article = None
        try:
            article = art.objects.get(id=request.data['id'])
        except:
            pass
        if (request.user.is_superuser or request.user.id == article.author.id):
            if article:
                article.keyword = request.data['keywords']
                article.save()
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

class Download (APIView):
    def get(self, request):

        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        article = None
        try:
            article = art.objects.get(id=request.data['id'])
        except:
            pass

        if article:

            file = article.article
            filepath = file.path

            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)