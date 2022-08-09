from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from TP_SD.views import home
from . import APIs
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('search/', views.index, name='index'),
    path('upload/', views.uploadpage, name='uploadpage'),
    path('api/delete/', APIs.DeleteArt.as_view(), name='deletearticle'),
    path('api/download/', APIs.Download.as_view(), name='downloadarticle'),
    path('api/edit/', APIs.EditMeta.as_view(), name='editmetadata'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)