from django.urls import path

from . import views

app_name = "forum"


urlpatterns = [
    path("", views.TopicsListView.as_view(), name="index"),
    path(
        "<int:topic_id>/delete/",
        views.TopicDeleteView.as_view(),
        name="delete_topic",
    ),
    path(
        "<int:topic_id>/update/",
        views.TopicUpdateView.as_view(),
        name="update_topic",
    ),
    path("add/", views.TopicCreateView.as_view(), name="create_topic"),
    path(
        "<int:topic_id>/posts/",
        views.PostsListView.as_view(),
        name="topic_posts",
    ),
    path(
        "<int:topic_id>/posts/<int:post_id>/delete/",
        views.PostDeleteView.as_view(),
        name="delete_post",
    ),
    path(
        "<int:topic_id>/posts/<int:post_id>/update/",
        views.PostUpdateView.as_view(),
        name="update_post",
    ),
    path(
        "<int:pk>/posts/add/",
        views.PostCreateView.as_view(),
        name="create_post",
    ),
]
