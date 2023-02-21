from dataclasses import dataclass

from django.contrib.auth import get_user_model

from app_authentication.models import Profile

User = get_user_model()


@dataclass
class GetProfile:
    user: User  # type: ignore

    def __call__(self) -> Profile:
        profile, _ = Profile.objects.get_or_create(user=self.user)
        return profile
