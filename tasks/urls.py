from django.urls import path
from .views import TaskList,TaskAdd

app_name = "tasks"


urlpatterns = [
    path("", TaskList.as_view(),name="home" ),
    path("add/", TaskAdd.as_view(), name="add")
]
