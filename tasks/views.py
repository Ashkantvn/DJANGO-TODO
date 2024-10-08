
from django.shortcuts import render,HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
# Create your views here
class TaskList(LoginRequiredMixin,ListView):
    template_name="tasks/task_list.html"
    model = Task
    context_object_name = "tasks"



class TaskAdd(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['title','description']
    success_url = reverse_lazy('tasks:home')
    template_name = "tasks/task_add.html"       

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    

class TaskDetails(LoginRequiredMixin,DetailView):
    model= Task
    template_name = "tasks/task_details.html"


class TaskDelete(DeleteView):
    model = Task
    template_name = "tasks/task_delete.html"
    success_url = reverse_lazy("tasks:home")
    

    