from django.urls import path, include
from . import views
# from rest_framework import routers
# from .api.v1 import views


app_name = "tasks"

urlpatterns = [
    path("", views.TaskList.as_view(), name="home"),
    path("add/", views.TaskAdd.as_view(), name="add"),
    path("<int:pk>/", views.TaskDetails.as_view(), name="details"),
    path("<int:pk>/delete", views.TaskDelete.as_view(), name="delete"),
    path("<int:pk>/update", views.TaskUpdate.as_view(), name="update"),
    path("<int:pk>/edit", views.TaskEdit.as_view(), name="edit"),
    path("api/v1/", include("tasks.api.v1.urls")),
]
