from typing import Any

from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.detail import DetailView

from app_authentication.logic_auth.logic_profile import GetProfile
from app_authentication.models import Profile


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = "app_authentication/user_profile.html"

    def get_object(self, queryset: Any = None) -> Any:
        return GetProfile(user=self.request.user)()


class UserProfileUpdate(UpdateView):
    model = Profile
    template_name = "app_authentication/profile_update.html"
    fields = [
        "name",
        "surname",
        "bio",
    ]
    success_url = reverse_lazy("auth:user_profile")

    def get_object(self, queryset: Any = None) -> Any:
        return GetProfile(user=self.request.user)()
