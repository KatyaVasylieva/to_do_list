from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from to_do.models import Task, Tag


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


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    template_name = "to_do/tag_form.html"
    success_url = reverse_lazy("to-do:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "to_do/tag_form.html"
    success_url = reverse_lazy("to-do:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("to-do:tag-list")


def toggle_complete_task(request, pk):
    task = Task.objects.get(id=pk)
    if (
        task.is_done is True
    ):
        task.is_done = False
    else:
        task.is_done = True
    task.save()
    return HttpResponseRedirect(reverse_lazy("to-do:index"))
