from django.urls import path
from .views import HomePostListView, PostDetailView, PostCreateView, PostUpadteView

app_name = "blog"

urlpatterns = [
    path("home/", HomePostListView.as_view(), name="home"),
    path("create/", PostCreateView.as_view(), name="post_create"),
    path("detail/<int:pk>/<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
    path("update/<int:pk>/<slug:slug>/", PostUpadteView.as_view(), name="post_update"),
]
