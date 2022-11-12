from django.urls import path
from .views import user_signUp, user_login, profile, profile_edit, user_logout

app_name = "account"

urlpatterns = [
    path("signup/",user_signUp, name='signup'),
    path("login/",user_login, name='login'),
    path("logout/",user_logout, name='logout'),
    path("profile/",profile, name='profile'),
    path("profileedit/",profile_edit, name='profileedit'),
]
