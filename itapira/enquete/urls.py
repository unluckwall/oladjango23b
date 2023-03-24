from django.urls import path

from . import views

urlpatter = [
    path('', views.index, nome='index'),
]