from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


class Feed(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to="feed_images/", null=True, blank=True)
    video = models.FileField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name="liked_feeds", blank=True)

    def __str__(self):
        return self.title

    def get_likes_count(self):
        return self.likes.count()


class Comment(models.Model):
    feed = models.ForeignKey(Feed, related_name="comments", on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.text
