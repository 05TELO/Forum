from django import forms
from django.http import HttpResponse
from django.urls import reverse
from django.urls import reverse_lazy
from django.views import generic

from app_forum.models import Post
from app_forum.models import Topic



class PostCreateView(generic.CreateView):
    model = Post
    fields = ["text"]
    success_url = reverse_lazy("forum:index")
    template_name = "app_forum/posts/create_post.html"

    def form_valid(self, form: forms.ModelForm) -> HttpResponse:
        topic = self.kwargs["topic_id"]
        self.success_url = reverse("forum:topic_posts", args=[topic])
        form.instance.topic = Topic.objects.get(id=topic)
        rs = super().form_valid(form)
        return rs


class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy("forum:index")
    template_name = "app_forum/posts/delete_post.html"
    pk_url_kwarg = "post_id"

    def form_valid(self, form: forms.ModelForm) -> HttpResponse:
        topic = self.kwargs["topic_id"]
        self.success_url = reverse("forum:topic_posts", args=[topic])
        rs = super().form_valid(form)
        return rs


class PostUpdateView(generic.UpdateView):
    model = Post
    fields = ["text"]
    success_url = reverse_lazy("forum:index")
    template_name = "app_forum/posts/update_post.html"
    pk_url_kwarg = "post_id"

    def form_valid(self, form: forms.ModelForm) -> HttpResponse:
        topic = self.kwargs["topic_id"]
        self.success_url = reverse("forum:topic_posts", args=[topic])
        rs = super().form_valid(form)
        return rs
