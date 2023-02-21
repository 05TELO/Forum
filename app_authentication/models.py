from typing import Any

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Profile(models.Model):
    name: Any = models.CharField(max_length=50, blank=True, null=True)
    surname: Any = models.CharField(max_length=50, blank=True, null=True)
    bio: Any = models.TextField(null=True, blank=True)
    user: Any = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="+"
    )

    def __str__(self) -> str:
        return str(self.user)
