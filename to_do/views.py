from django.views import generic

from to_do.models import Task


class Index(generic.ListView):
    queryset = Task.objects.order_by(["-is_done", "-created_time"])
    template_name = "to_do/index.html"
