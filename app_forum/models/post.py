from django.db import models
from .topic import Topic


class Post(models.Model):
    date = models.DateTimeField(auto_now_add=True, null=True)
    text = models.TextField(max_length=1000)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="topic")

    def __str__(self):
        return '1111111'