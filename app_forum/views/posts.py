from django import forms
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


from app_forum.logic_forum import get_reverse_url
from app_forum.models import Post
from app_forum.models import Topic

url_login = reverse_lazy("auth:login")



class PostCreateView(LoginRequiredMixin, generic.CreateView):
    login_url = url_login
    model = Post
    fields = ["text"]
    success_url = reverse_lazy("forum:index")
    template_name = "app_forum/posts/create_post.html"

    def form_valid(self, form: forms.ModelForm) -> HttpResponse:
        topic = self.kwargs["topic_id"]
        form.instance.author = self.request.user
        self.success_url = get_reverse_url(topic)
        form.instance.topic = Topic.objects.get(id=topic)
        rs = super().form_valid(form)
        return rs


class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    login_url = url_login
    model = Post
    success_url = reverse_lazy("forum:index")
    template_name = "app_forum/posts/delete_post.html"
    pk_url_kwarg = "post_id"

    def form_valid(self, form: forms.ModelForm) -> HttpResponse:
        topic = self.kwargs["topic_id"]
        self.success_url = get_reverse_url(topic)
        rs = super().form_valid(form)
        return rs


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    login_url = url_login
    model = Post
    fields = ["text"]
    success_url = reverse_lazy("forum:index")
    template_name = "app_forum/posts/update_post.html"
    pk_url_kwarg = "post_id"

    def form_valid(self, form: forms.ModelForm) -> HttpResponse:
        topic = self.kwargs["topic_id"]
        self.success_url = get_reverse_url(topic)
        rs = super().form_valid(form)
        return rs
