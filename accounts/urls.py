from django.urls import path
from django.urls import reverse_lazy
from django.views.generic.base import RedirectView ,TemplateView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .views import ProfileView

app_name = "accounts"

urlpatterns = [
    path("", RedirectView.as_view(url=reverse_lazy('accounts:login'),permanent=True)),
    path("login/", LoginView.as_view(template_name="accounts/login_page.html"), name="login"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("logout/", LogoutView.as_view(), name="logout")
]
