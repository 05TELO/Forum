from typing import Any
from typing import cast

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic

from app_forum.models import Topic

User = get_user_model()


class TopicForm(forms.Form):
    text = forms.CharField(label="Topic:")


class TopicsListView(generic.ListView):
    model = Topic
    template_name = "app_forum/index.html"
    extra_context = {"form": TopicForm()}

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        return ctx


class TopicCreateView(generic.CreateView):
    model = Topic
    fields = ["title"]
    success_url = reverse_lazy("forum:index")
    template_name = "app_forum/topics/create_topic.html"

    def form_valid(self, form: forms.ModelForm) -> HttpResponse:
        rs = super().form_valid(form)

        return rs