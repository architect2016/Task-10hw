from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from . import views
from .forms import LoginForm

app_name = "users"

urlpatterns = [
    path("signup/", views.RegisterView.as_view(), name="signup"),
    path("signin/", LoginView.as_view(template_name="users/login.html", form_class=LoginForm), name="signin"),
    path("logout/", LogoutView.as_view(template_name="users/logout.html"), name="logout"),
]