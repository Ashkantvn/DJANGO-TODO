from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.shortcuts import redirect
from django.contrib.auth import login

# Create your views here.


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"


class RegisterView(CreateView):
    template_name = "accounts/register_page.html"
    form_class = RegisterForm
    success_url = reverse_lazy("accounts:profile")

    def form_valid(self, form):
        login(self.request, form.save())
        return redirect("accounts:profile")
