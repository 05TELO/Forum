from django.urls import path

from . import views

app_name = "forum"


urlpatterns = [
    path("", views.TopicsListView.as_view(), name="index"),
    path("add/", views.TopicCreateView.as_view(), name="create_topic"),
    path("<int:pk>/posts/", views.PostsListView.as_view(), name="topic_posts"),
    path(
        "<int:pk>/posts/add/",
        views.PostCreateView.as_view(),
        name="create_post",
    ),
]
