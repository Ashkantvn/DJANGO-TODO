from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Task


# Create your views here
class TaskList(LoginRequiredMixin, ListView):
    template_name = "tasks/task_list.html"
    model = Task
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.filter(creator=self.request.user)


class TaskAdd(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["title", "description"]
    success_url = reverse_lazy("tasks:home")
    template_name = "tasks/task_add.html"

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class TaskDetails(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "tasks/task_details.html"

    def get(self, request, *args, **kwargs):
        task = self.get_object()
        if task.creator != self.request.user:
            return redirect("tasks:home")
        return super().get(request, *args, **kwargs)


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "tasks/task_delete.html"
    success_url = reverse_lazy("tasks:home")

    def dispatch(self, request, *args, **kwargs):
        task = self.get_object()
        if task.creator != self.request.user:
            return redirect("tasks:home")
        return super().dispatch(request, *args, **kwargs)


class TaskUpdate(LoginRequiredMixin, View):
    def get(self, request, pk):
        task = Task.objects.get(pk=pk)
        if task.creator == self.request.user:
            task.done = not task.done
            task.save()
        return redirect("tasks:home")


class TaskEdit(UpdateView):
    model = Task
    template_name = "tasks/task_add.html"
    fields = ["title", "description"]

    def get(self, request, *args, **kwargs):
        task = self.get_object()
        if task.creator != self.request.user:
            return redirect("tasks:home")
        return super().get(request, *args, **kwargs)
