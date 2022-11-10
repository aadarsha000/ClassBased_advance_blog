from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def user_signUp(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(user, request)
                return redirect("blog:home")
    form = UserCreationForm()
    return redirect(request, "account/signup.html", {"form":form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(user, request)
                return redirect("blog:home")
    form = AuthenticationForm()
    return redirect(request, "account/login.html", {"form":form})


@login_required(login_url="account/login")
def user_logout(request):
    logout(request)
    return redirect("blog:home")
