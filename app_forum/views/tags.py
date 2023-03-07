from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views import generic
from taggit.models import Tag

from app_forum.models import Topic


class TagView(generic.View):
    def get(self, request: HttpRequest, slug, *args, **kwargs):
        tag = get_object_or_404(Tag, slug=slug)
        topics = Topic.objects.filter(tag=tag)
        common_tags = Topic.tag.most_common()
        return render(
            request,
            "app_forum/tags/tag.html",
            context={
                "title": f"#{tag}",
                "topics": topics,
                "common_tags": common_tags,
            },
        )
