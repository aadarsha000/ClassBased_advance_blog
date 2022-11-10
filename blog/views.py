from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required


# fuction based view

#home view that show list of post
def home(request):
    posts = Post.objects.all().filter(status="PUBLISHED")
    return render(request, "blog/index.html", {"posts":posts})




# detail view that show clicked post detail
def post_detail(request, id, slug, category):
    post = get_object_or_404(Post, id=id, slug=slug, status="PUBLISHED")
    posts = Post.objects.all().filter(status="PUBLISHED", category=category)
    context ={}
    context["post"]=post
    context["posts"]=posts
    return render(request, "blog/postdetail.html", context)



# Create the post by only login user
@login_required(login_url="account/login")
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author = request.user
            post.slug = slugify(post.title)
            post.save()
            return redirect("blog:home")
    else:
        form = PostForm()
    context = {"form":form}
    return render(request, "blog/postcreate.html", context)



# update the existing view
# @login_required(login_url="account/login")
def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
    else:
        form = PostForm(instance=post)
    context = {"form":form}
    return render(request, "blog/postudate.html", context)

