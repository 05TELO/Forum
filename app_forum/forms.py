from django import forms

from .models import Post
from .models import Topic


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["text"]


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = "__all__"
