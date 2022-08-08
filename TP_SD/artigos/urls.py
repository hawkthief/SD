from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.uploadpage, name='uploadpage'),
    path('manage/', views.manageusers, name='manageusers'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)