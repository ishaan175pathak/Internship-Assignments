from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Votes

# Create your views here.

def index(request):
    if request.method == "GET":
        return render(request, "home/home.html")
    
    elif request.method == "POST":

        email = request.POST.get('inputEmail')
        password = request.POST.get('inputPassword')
        
        try:
            username = email[:email.rindex("@")]
            user = authenticate(request, username = username, password = password)
            if user:
                login(request, user)
                return redirect("home")
            else:
                return render(request, "home/home.html", {"target": 0})
        except:
            return redirect("home")

def signup(request):
    if request.method == "GET":
        return render(request, "signup/signup.html")

    elif request.method == "POST":
        email = request.POST.get("emailField")
        password = request.POST.get("passwordField")
        
        try:
            user = User.objects.create_user(username=email[:email.rindex("@")], email=email, password=password)
            user.save()
            
            return redirect("home")
        
        except:
            return render(request, "signup/signup.html")

def Logout(request):
    logout(request)
    return redirect("/")

def vote(request):
    if request.method == "POST":
        currentUser = request.user.username
        vote = str(request.POST.get("vote")).strip()
        obj = Votes(username = currentUser, vote = vote)
        try:
            obj.save()
            print("Object Saved")
        except:
            print("not saved")

        return redirect("/")