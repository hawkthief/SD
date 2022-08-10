from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .forms import artForm
from .models import art, usuario
from TP_SD.settings import BASE_URL
from TP_SD.secrets import *
from django.core.mail import send_mail
from .forms import searchForm
from .views import download_file
import pandas as pd

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

            url = BASE_URL + "artigos/download/" + str(request.data['id'])
            return Response(url, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_404_NOT_FOUND)

class email(APIView):

    def get(self, request):

        return Response(status=status.HTTP_200_OK)
    def post(self, request):
        email = request.data["email"]

        sendmail(email)

def sendmail(email):
    subject = "Your account"
    msg = "Your account was made sucessfully"
    try:
        send_mail(
            subject=subject,
            message=msg,
            from_email=email,
            recipient_list=[EMAIL_HOST_USER],
            auth_password=EMAIL_HOST_PASSWORD,
        )
    except:
        pass