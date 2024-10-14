from django.urls import path, include
from django.urls import reverse_lazy
from django.views.generic.base import RedirectView
from django.contrib.auth.views import LoginView, LogoutView
# from django.contrib.auth.mixins import LoginRequiredMixin
from .views import ProfileView, RegisterView

app_name = "accounts"

urlpatterns = [
    path(
        "",
        RedirectView.as_view(
            url=reverse_lazy("accounts:login"),
            permanent=True)),
    path(
        "login/",
        LoginView.as_view(template_name="accounts/login_page.html"),
        name="login",
    ),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("api/v1/", include("accounts.api.v1.urls")),
]
