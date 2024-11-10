from django.contrib import admin
from django.urls import path
from .views import *

app_name = "user2"

urlpatterns = [
    path("register/",register,name = "register"),
    path("login/",login2,name = "login2"),
    path("logOut/",logOut,name = "logOut"),
]