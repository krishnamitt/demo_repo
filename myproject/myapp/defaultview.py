from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse

def login_page(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)   # creates session
            return redirect("/myapp/home/")
    return render(request, "login.html")

def home(request):
    if not request.user.is_authenticated:
        return HttpResponse("Not logged in")
    return HttpResponse(f"Hello {request.user.username}")