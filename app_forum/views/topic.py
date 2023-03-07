from typing import Any

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic

from app_forum.forms import TopicForm
from app_forum.models import Topic

User = get_user_model()
url_login = reverse_lazy("auth:login")


class TopicsListView(generic.ListView):
    paginate_by = 6
    model = Topic
    template_name = "app_forum/index.html"
    extra_context = {"form": TopicForm()}

    def get_queryset(self) -> Any:
        qs = super().get_queryset()
        search = self.request.session.get("search")
        if search:
            return qs.filter(title__icontains=search)
        return qs


class TopicSearchView(generic.FormView):
    form_class = forms.Form
    success_url = reverse_lazy("forum:index")
    http_method_names = ["post"]

    def form_valid(self, form: forms.Form) -> HttpResponse:
        search = self.request.POST["search"]
        self.request.session["search"] = search
        return super().form_valid(form)


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    login_url = url_login
    model = Topic
    fields = ["title", "tag"]
    success_url = reverse_lazy("forum:index")
    template_name = "app_forum/topics/create_topic.html"

    def form_valid(self, form: forms.ModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        rs = super().form_valid(form)
        return rs


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    login_url = url_login
    model = Topic
    success_url = reverse_lazy("forum:index")
    template_name = "app_forum/topics/delete_topic.html"
    pk_url_kwarg = "topic_id"


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    login_url = url_login
    model = Topic
    fields = ["title", "tag"]
    success_url = reverse_lazy("forum:index")
    template_name = "app_forum/topics/update_topic.html"
    pk_url_kwarg = "topic_id"
