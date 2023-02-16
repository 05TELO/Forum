from django.contrib import admin
from app_forum.models import Topic, Post
# Register your models here.
@admin.register(Topic)
class TopicModelAdmin(admin.ModelAdmin):  # noqa: F811
    pass

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    pass