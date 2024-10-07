
from django.shortcuts import render,HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
# Create your views here
class TaskList(LoginRequiredMixin,ListView):
    template_name="tasks/task_list.html"
    model = Task
    context_object_name = "tasks"
       