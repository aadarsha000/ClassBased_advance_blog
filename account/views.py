from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UsercreateFrom
from .forms import ProfileForm
from .models import Profile
from blog.models import Post
# Create your views here.


def user_signUp(request):
    if request.method == "POST":
        form = UsercreateFrom(request.POST)
        if form.is_valid():
            user = form.save()            
            login(request, user)
            return redirect("blog:home")
        else:
            form = UsercreateFrom(request.POST)
    form = UsercreateFrom()
    return render(request, "account/signup.html", {"form":form})


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
    return render(request, "account/login.html", {"form":form})


@login_required(login_url="account:login")
def user_logout(request):
    logout(request)
    return redirect("blog:home")

@login_required(login_url="account:login")
def profile_edit(request):
    user = request.user
    profile = Profile.objects.filter(user=user)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()            
            return redirect("blog:home")
    form = ProfileForm(instance=request.user.profile)
    return render(request, "account/profileedit.html", {"form":form})

@login_required(login_url="account:login")
def profile(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    post = get_list_or_404(Post, author=user)
    context = {
        'profile':profile,
        'post':post
    }
    return render(request, 'account/profile.html',context)

