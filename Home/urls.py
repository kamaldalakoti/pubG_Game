from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [

    path('',views.home,name='home'),
    path('Home',views.home,name='home'),
    path('Registration',views.Registration,name='registration'),
    path('About',views.about,name='about'),
    path('',views.home,name='home'),
]
