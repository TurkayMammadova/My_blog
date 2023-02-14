from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login,authenticate,logout




# Create your views here.

def register(request):

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username =username)
        newUser.set_password(password)

        newUser.save()
        auth_login(request,newUser)
        messages.info(request,"Başarıyla Kayıt Oldunuz...")

        return redirect("index")
    context = {
            "form" : form
        }
    return render(request,"register.html",context)



def login(request):
    form=LoginForm(request.POST or None)
    context={'form':form}

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user=authenticate(username=username, password=password)

        if user is None:
            messages.info(request,'Username ve ya password yalnis...')
            return render(request,"login.html",context)

        messages.success(request,"Başarıyla Giriş Yaptınız")
        auth_login(request,user)
        return redirect("index")
    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    messages.success(request,'Basariyla cikis yaptiniz')
    return redirect('index')


    