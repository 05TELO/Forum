from typing import Any
from typing import cast

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic

from app_forum.models import Topic, Post

User = get_user_model()


class PostForm(forms.Form):
    text = forms.CharField(label="Topic:")


class PostsListView(generic.ListView):
    model = Post
    template_name = "app_forum/topics/topic_posts.html"
    extra_context = {"form": PostForm()}

    def get_queryset(self) -> Any:
        qs = super().get_queryset()
        x = qs.filter(topic=self.kwargs["pk"])
        return qs.filter(topic=self.kwargs["pk"])


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        return ctx


