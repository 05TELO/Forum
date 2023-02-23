from django.contrib import admin

from app_forum.models import Post
from app_forum.models import Topic


# Register your models here.
@admin.register(Topic)
class TopicModelAdmin(admin.ModelAdmin):  # noqa: F811
    list_display = ["title", "date"]


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["text", "date"]
