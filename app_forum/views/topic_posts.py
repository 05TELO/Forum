from typing import Any

from django.contrib.auth import get_user_model
from django.views import generic

from app_forum.models import Post
from app_forum.forms import PostForm

User = get_user_model()




class PostsListView(generic.ListView):
    model = Post
    template_name = "app_forum/topics/topic_posts.html"
    extra_context = {"form": PostForm()}

    def get_queryset(self) -> Any:
        qs = super().get_queryset()
        return qs.filter(topic=self.kwargs["topic_id"])

