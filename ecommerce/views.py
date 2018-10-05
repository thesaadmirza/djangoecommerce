from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,get_user_model
from .forms import ContactForm,LoginForm,RegisterForm
def homePage(request):
    context = {
        "title" : "HEy this is the title",
    }
    return render(request,'homePage.html',context)

def LoginPage(request):
    form = LoginForm(request.POST or None)
    context = {
        "form" : form,
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user     = authenticate(request,username=username,password=password)
        if user is not None:
            print(request.user.is_authenticated)
            login(request,user)
            return redirect("/login")
        else:
            print("Error")
    return render(request,'auth/login.html',context)
User = get_user_model()
def RegisterPage(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form" : form,
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        new_user = User.objects.create_user(username,email,password)
        print(new_user)

    else:
        print("Error")
    return render(request,"auth/register.html",context)

def contactPage(request):
    contactform = ContactForm(request.POST or None)
    context = {
        "title" : "this is contact page",
        "form" : contactform,
    }
    if contactform.is_valid():
        print(contactform.cleaned_data)
    return render(request,'contact/view.html',context)

def aboutPage(request):
    context = {
        "title" : "HEy this is the about Page",
    }
    return render(request,'homePage.html',context)
    