from typing import Any

from django import forms
from django.contrib.auth import get_user_model
from django.views import generic

from app_forum.models import Post

User = get_user_model()


class PostForm(forms.Form):
    text = forms.CharField(label="Topic:")


class PostsListView(generic.ListView):
    model = Post
    template_name = "app_forum/topics/topic_posts.html"
    extra_context = {"form": PostForm()}

    def get_queryset(self) -> Any:
        qs = super().get_queryset()
        return qs.filter(topic=self.kwargs["topic_id"])

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        return ctx
