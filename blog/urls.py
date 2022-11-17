from django.urls import path
from .views import post_create, post_update
from .views import HomePostListView, PostDetailView

app_name = "blog"

urlpatterns = [
    path("home/", HomePostListView.as_view(), name="home"),
    path("create/", post_create, name="post_create"),
    path("detail/<int:pk>/<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
    path("update/", post_update, name="post_update"),
]
