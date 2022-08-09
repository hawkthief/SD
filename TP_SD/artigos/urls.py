from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from TP_SD.views import home
from . import views

urlpatterns = [
    path('', home, name='index'),
    path('search/', views.index, name='index'),
    path('upload/', views.uploadpage, name='uploadpage'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)