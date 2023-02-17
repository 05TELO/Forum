from typing import Any

from django.db import models


class Topic(models.Model):
    title: Any = models.TextField(max_length=1312)
    date: Any = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.title}"
