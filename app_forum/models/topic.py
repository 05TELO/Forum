from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator


class Topic(models.Model):
    title = models.TextField(max_length=1312)
    date = models.DateTimeField(auto_now_add=True, null=True)

