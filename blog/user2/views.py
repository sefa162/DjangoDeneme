from django.shortcuts import render
from user.views import *
# Create your views here.
def register(request):
    form = RegisterForm()

    context = {
        "form"  : form
    }

    return render(request,"register.html",context)
def login(request):
    pass
def logOut(request):
    pass
