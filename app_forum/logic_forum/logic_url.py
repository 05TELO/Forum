from django.urls import reverse


def get_reverse_url(topic: int):
    return reverse("forum:topic_posts", args=[topic])
