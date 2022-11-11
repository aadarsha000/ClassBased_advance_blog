from django.urls import path
from .views import post_create, post_detail, post_update, home

app_name = "blog"

urlpatterns = [
    path("home/", home, name="home"),
    path("create/", post_create, name="post_create"),
    path("detail/<int:id>/<slug:slug>/<int:category>/", post_detail, name="post_detail"),
    path("update/", post_update, name="post_update"),
]
