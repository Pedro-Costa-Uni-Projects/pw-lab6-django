from django.shortcuts import render
from . import views
from django.urls import path

app_name = "website"

urlpatterns = [
    path('home', views.home_page_view, name='home'),
    path('pag1', views.page_one_view, name='page1'),
    path('pag2', views.page_two_view, name='page2')
]
