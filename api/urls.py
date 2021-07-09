from django.urls import path

from .views import *
urlpatterns = [
    path('covid/<sigla>', EstadoDados.as_view()),
]