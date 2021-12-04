from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ,name = 'index'),
    path('survey', views.survey, name = 'survey'),
    path('dbtest', views.dbtest, name = 'dbtest'),
    path('recommend', views.recommend, name = 'recommend'),
]