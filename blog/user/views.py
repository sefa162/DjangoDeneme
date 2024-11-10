from django.shortcuts import render,redirect
from . forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

# Create your views here.

def register(request):
    if (request.user.is_authenticated):
        messages.warning(request,"Giriş Yapılıyken Kayıt Olamazsın")
        return redirect("index")

    form = RegisterForm(request.POST or None) # POST içeriği varsa al yoksa none dön

    
    if (form.is_valid()):

        username = form.cleaned_data.get("username") # username bilgisi form'un döndürdüğü sözlükten çekilerek username değişkenine atılıyor
        password = form.cleaned_data.get("password") # password bilgisi form'un döndürdüğü sözlükten çekilerek passsword değişkenine atılıyor
        newUser = User(username = username) # Bilgilerle Yeni User nesnesi oluşturuluyor
        newUser.set_password(password) # Parolayı Şifrelemek İçin Bu Yöntemi Kullanıyoruz
        newUser.save() # Kayıt etme işlemi
        login(request,newUser) # Kullanıcıyı Login (Giriş) Yapma İşlemi
        messages.success(request,"Başarılı Bir Şekilde Kayıt Oldunuz!")
        return redirect("index") # index sayfasına redirect (geri dönme) işlemi
    

    context = {"form" : form}
    return render(request,"register.html",context)





def login2(request):
    if (request.user.is_authenticated):
        messages.warning(request,"Giriş Yapıldıkan Sonra Giriş Yapılamaz")
        return redirect("index")
    form = LoginForm(request.POST or None)
    context = {"form" : form}

    if (form.is_valid()):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username,password = password)
        
        if (user is None):
            messages.info(request,"Kullanıcı Adı Veya Parola Hatalı")
            return render(request,"login.html",context)
        messages.success(request,"Başarıyla Giriş Yaptınız")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)




def logOut(request):
    if (request.user.is_authenticated):
        logout(request)
        messages.success(request,"Başarıyla Çıkış Yaptınız")
        return redirect("index")
    messages.warning(request,"Giriş Yapmadan Çıkış Yapamazsın!")
    return redirect("user2:login2")


def dashboard(request):
    return render(request,"dashboard.html")