from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Comment
from .forms import PostForm, CommentForm
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# fuction based view

#home view that show list of post
# def home(request):
#     posts = Post.objects.all().filter(status="PUBLISHED")
#     category = Category.objects.all()
#     paginator = Paginator(posts, 2)
#     page_number = request.GET.get('page', 1)
#     try:
#         page_obj = paginator.page(page_number)
#     except PageNotAnInteger:
#         # if page is not an integer, deliver the first page
#         page_obj = paginator.page(1)
#     except EmptyPage:
#         # if the page is out of range, deliver the last page
#         page_obj = paginator.page(paginator.num_pages)
#     context = {
#         "posts":posts,
#         "category":category,
#         "page_obj":page_obj,
#     }
#     return render(request, "blog/index.html", context)

# home view using class
class HomePostListView(ListView):
    model = Post
    paginate_by = 2
    context_object_name = "posts"
    template_name = "blog/index.html"

    def get_queryset(self):
        return Post.objects.all().filter(status="PUBLISHED")
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context




# detail view that show clicked post detail 
# def post_detail(request, id, slug, category):
#     context ={}
#     post = get_object_or_404(Post, id=id, slug=slug, status="PUBLISHED")
#     posts = Post.objects.all().filter(category=category).exclude(id=id)
#     comments = Comment.objects.all().filter(post=id)
#     new_comment=None
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         print("hello")
#         if form.is_valid():
#             new_comment=form.save(commit=False)
#             new_comment.user = request.user
#             new_comment.post = post
#             print("hi")
#             new_comment.save()
#             print("hello")
#         else:
#             print("error")
#     else:
#         form = CommentForm()
#         print("else")
    
#     context['comments']=comments
#     context['form']=form
#     context["post"]=post
#     context["posts"]=posts
#     return render(request, "blog/postdetail.html", context)


# classs based post detail view
class PostDetailView(DetailView, FormMixin):
    model = Post
    context_object_name = "post"
    template_name = "blog/postdetail.html"
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy("blog:post_detail", kwargs={'pk':self.object.id, 'slug':self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.all().filter(post=self.kwargs['pk'])
        cat = get_object_or_404(Post, id=self.kwargs['pk'])
        context["posts"] = Post.objects.all().filter(category=cat.category)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = self.object
        form.save()
        return super().form_valid(form)

    


# Create the post by only login user
# @login_required(login_url="account/login")
# def post_create(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post=form.save(commit=False)
#             post.author = request.user
#             post.slug = slugify(post.title)
#             post.save()
#     else:
#         form = PostForm()
#     context = {"form":form}
#     return render(request, "blog/postcreate.html", context)

class PostCreateView(CreateView):
    template_name = "blog/postcreate.html"
    form_class = PostForm

    def get_success_url(self):
        return reverse_lazy("blog:home")

    def post(self, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        form.save()
        return super().form_valid(form)


# update the existing view
# @login_required(login_url="account/login")
# def post_update(request, id):
#     post = get_object_or_404(Post, id=id)
#     if request.method == "POST":
#         form = PostForm(request.POST,instance=post)
#         if form.is_valid():
#             form.save()
#     else:
#         form = PostForm(instance=post)
#     context = {"form":form}
#     return render(request, "blog/postudate.html", context)

class PostUpadteView(UpdateView):
    model = Post
    template_name = "blog/postUpdate.html"
    form_class = PostForm
    context_object_name = 'form'
    def get_success_url(self):
        return reverse_lazy("blog:home")

