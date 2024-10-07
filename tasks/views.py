
from django.shortcuts import render,HttpResponse
from django.views.generic.base import TemplateView
# Create your views here.
class TaskList(TemplateView):
    template_name="tasks/task_list.html"
    