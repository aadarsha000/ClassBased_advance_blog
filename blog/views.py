from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from .forms import PostForm
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



# fuction based view

#home view that show list of post
def home(request):
    posts = Post.objects.all().filter(status="PUBLISHED")
    category = Category.objects.all()
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page', 1)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)
    context = {
        "posts":posts,
        "category":category,
        "page_obj":page_obj,
    }
    return render(request, "blog/index.html", context)




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

