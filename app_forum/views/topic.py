from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views import generic

from app_forum.forms import TopicForm
from app_forum.models import Topic

User = get_user_model()


class TopicsListView(generic.ListView):
    model = Topic
    template_name = "app_forum/index.html"
    extra_context = {"form": TopicForm()}


class TopicCreateView(generic.CreateView):
    model = Topic
    fields = ["title"]
    success_url = reverse_lazy("forum:index")
    template_name = "app_forum/topics/create_topic.html"


class TopicDeleteView(generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("forum:index")
    template_name = "app_forum/topics/delete_topic.html"
    pk_url_kwarg = "topic_id"


class TopicUpdateView(generic.UpdateView):
    model = Topic
    fields = ["title"]
    success_url = reverse_lazy("forum:index")
    template_name = "app_forum/topics/update_topic.html"
    pk_url_kwarg = "topic_id"
