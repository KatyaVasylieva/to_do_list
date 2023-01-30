from django.urls import reverse
from django.views import generic

from to_do.models import Task


class Index(generic.ListView):
    queryset = Task.objects.order_by("-is_done", "-created_time")
    template_name = "to_do/index.html"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    template_name = "to_do/task_create_form.html"

    # def get_success_url(self):
    #     return reverse("to-do:index", kwargs={"pk": self.object.pk})
