from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

urlpatterns = [
    path("login/", LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="registration/logout.html"), name="logout"),
]

app_name = "accounts"
