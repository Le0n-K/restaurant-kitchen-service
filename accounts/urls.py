from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from accounts.views import register


urlpatterns = [
    path("login/", LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="registration/logout.html"), name="logout"),
    path("register/", register, name="register"),
]

app_name = "accounts"
