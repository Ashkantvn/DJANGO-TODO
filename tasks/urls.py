from django.urls import path
from .views import TaskList,TaskAdd,TaskDetails,TaskDelete,TaskUpdate,TaskEdit

app_name = "tasks"


urlpatterns = [
    path("", TaskList.as_view(),name="home" ),
    path("add/", TaskAdd.as_view(), name="add"),
    path("<int:pk>/", TaskDetails.as_view(), name="details"),
    path("<int:pk>/delete", TaskDelete.as_view(), name="delete"),
    path("<int:pk>/update", TaskUpdate.as_view(), name="update"),
    path("<int:pk>/edit", TaskEdit.as_view(), name="edit")
]
