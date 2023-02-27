from typing import Any

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic


User = get_user_model()
url_login = reverse_lazy("auth:login")


def handle_change_group(
    request: HttpRequest, user_id: int, group: str
) -> HttpResponse:
    user = User.objects.get(id=user_id)
    group = Group.objects.get(name=group)
    user.groups.clear()
    user.groups.add(group)
    return redirect("forum:manage_users")


class UsersListView(generic.ListView):
    model = User
    template_name = "app_forum/manage_users/manage_users.html"

    def get_queryset(self) -> Any:
        qs = super().get_queryset()
        search = self.request.session.get("search")
        if search:
            return qs.filter(username__icontains=search)
        return qs


class UserSearchView(generic.FormView):
    form_class = forms.Form
    success_url = reverse_lazy("forum:manage_users")
    http_method_names = ["post"]

    def form_valid(self, form: forms.Form) -> HttpResponse:
        search = self.request.POST["search"]
        self.request.session["search"] = search
        return super().form_valid(form)
