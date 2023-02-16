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

class PostForm(forms.Form):
    text = forms.CharField(label="Post :")

class PostCreateView(generic.CreateView):
    model = Post
    fields = ["text"]
    success_url = reverse_lazy("forum:index")
    template_name = "app_forum/posts/create_post.html"

    def form_valid(self, form: forms.ModelForm) -> HttpResponse:
        topic = self.kwargs["pk"]
        form.instance.topic = Topic.objects.get(id=topic)
        rs = super().form_valid(form)
        return rs

