from django.contrib import admin
from django.urls import path
from .views import * 
app_name = "article"


urlpatterns = [
    path('dashboard/',dashboard,name="dashboard"),
    path('addarticle/',addArticle,name="addarticle"),   
    path('article/<int:id>',detail,name = "detail"),
    path('delete/<int:id>',deleteArticle,name="delete"),
    path('update/<int:id>',updateArticle,name="update"),
    path('comment/<int:id>',addComment,name="comment"),
    path('',articles,name="articles"),
]