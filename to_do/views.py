from django.urls import reverse, reverse_lazy
from django.views import generic

from to_do.models import Task


class Index(generic.ListView):
    queryset = Task.objects.order_by("-is_done", "-created_time")
    template_name = "to_do/index.html"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    template_name = "to_do/task_form.html"
    success_url = reverse_lazy("to-do:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    template_name = "to_do/task_form.html"
    success_url = reverse_lazy("to-do:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("to-do:index")
