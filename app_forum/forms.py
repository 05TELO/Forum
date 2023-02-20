from django import forms
from .models import Post, Topic


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text']


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title']
