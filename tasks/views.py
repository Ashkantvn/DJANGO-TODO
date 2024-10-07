
from django.shortcuts import render,HttpResponse
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
# Create your views here.
class TaskList(LoginRequiredMixin,TemplateView):
    template_name="tasks/task_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Task.objects.all()
        return context
       