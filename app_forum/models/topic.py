from typing import Any

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Topic(models.Model):
    title: Any = models.TextField(max_length=1312)
    date: Any = models.DateTimeField(auto_now_add=True, null=True)
    author: Any = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='+')

    def __str__(self):
        return f"{self.title}"
