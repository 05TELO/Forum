from typing import Any

from django.db import models

from .topic import Topic


class Post(models.Model):
    date: Any = models.DateTimeField(auto_now_add=True, null=True)
    text: Any = models.TextField(max_length=1000)
    topic: Any = models.ForeignKey(
        Topic, on_delete=models.CASCADE, related_name="posts"
    )

    def __str__(self):
        return "1111111"
