from typing import Any

from django import forms
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic

from app_forum.forms import PostForm
from app_forum.logic_forum import get_reverse_url
from app_forum.models import Post

User = get_user_model()


class PostsListView(generic.ListView):
    paginate_by = 6
    model = Post
    template_name = "app_forum/topics/topic_posts.html"
    extra_context = {"form": PostForm()}

    def get_queryset(self) -> Any:
        qs = super().get_queryset()
        search = self.request.session.get("search")
        if search:
            return qs.filter(
                topic=self.kwargs["topic_id"], text__icontains=search
            )
        return qs.filter(topic=self.kwargs["topic_id"])


class PostSearchView(generic.FormView):
    form_class = forms.Form
    success_url = reverse_lazy("forum:index")
    http_method_names = ["post"]

    def form_valid(self, form: forms.Form) -> HttpResponse:
        topic = self.kwargs["topic_id"]
        self.success_url = get_reverse_url(topic)
        search = self.request.POST["search"]
        self.request.session["search"] = search
        return super().form_valid(form)
