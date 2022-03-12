from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
       if not request.user.is_authenticated:
              return HttpResponseRedirect(reverse("login"))

def login_view(request):
       if request.method == "POST":
              username = request.POST["username"]
              password = request.POST["password"]
              user = authenticate(username=username, password=password)
              if user is not None:
                     login(request, user)
                     return render(request, "users/user.html")       
              else:
                     context = {
                            "message": "Invalid Credentials.",
                     }
                     return render(request, "users/login.html", context)
       return render(request, "users/login.html")


def logout_view(request):
       context = {
              "message": "Logged Out",
       }
       logout(request)
       return render(request, "users/login.html", context)