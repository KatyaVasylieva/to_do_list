from django.urls import path

from .views import Index, TaskCreateView

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
]

app_name = "to-do"
