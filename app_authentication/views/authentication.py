from django import forms
from django import http
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import Group
from django.db import IntegrityError
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from app_authentication.forms import LoginForm
from app_authentication.forms import SignUpForm
from app_authentication.models import Profile

url_redirect = reverse_lazy("forum:index")
User = get_user_model()


class UserAuthentication(generic.FormView):
    template_name = "app_authentication/login.html"
    form_class = LoginForm
    success_url = url_redirect

    def form_valid(self, form: forms.Form) -> http.HttpResponse:
        data = form.cleaned_data
        user = authenticate(
            self.request, username=data["username"], password=data["password"]
        )
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect(url_redirect)

            else:
                return HttpResponse("Disabled account")
        return HttpResponse("Invalid login")


def handle_user_logout(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect(url_redirect)


class UserSignUp(generic.FormView):
    template_name = "app_authentication/sing_up.html"
    form_class = SignUpForm
    success_url = reverse_lazy("auth:login")

    def form_valid(self, form: forms.Form) -> http.HttpResponse:
        data = form.cleaned_data

        try:
            new_user = User.objects.create_user(
                data["username"], data["email"], data["password"]
            )
        except IntegrityError:
            messages.error(self.request, "name is already in use")
            return redirect(reverse_lazy("auth:sing_up"))
        group = Group.objects.get(name="user")
        new_user.groups.add(group)
        new_user.save()
        profile_user = Profile(user=new_user)
        profile_user.save()
        return redirect(self.success_url)
