from django.urls import path
from . import views
from django.db import models
from django.contrib.auth.models import User


urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('view/', views.home, name='home'),
]
