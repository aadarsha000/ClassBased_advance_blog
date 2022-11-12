from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, UserCreationForm
from .models import Profile
from blog.models import Post
from django.contrib import messages
# Create your views here.


def user_signUp(request):
    context={}
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            return redirect("blog:home")
        else:
            context['form']=form
    else:
        form = UserCreationForm()
        context['form']=form
    return render(request, "account/signup.html", context)


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username, password)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("blog:home")
            else:
                messages.error(request, "invalid Username or Password 1")
        else:
            messages.error(request, "invalid Username or Password")
    form = AuthenticationForm()
    return render(request, "account/login.html", {"form":form})

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
    post = Post.objects.all().filter(author=user)
    context = {
        'profile':profile,
        'post':post
    }
    return render(request, 'account/profile.html',context)

