from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCountMixin, HitCount
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


<<<<<<< HEAD
class Feed(models.Model, HitCountMixin):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="author")
    title = models.CharField(max_length=100)
    context = models.TextField(blank=True)
    image = models.ImageField(blank=True,upload_to="photo/%Y/%m/%d")
    video = models.FileField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, default=0, related_name="likes_feed")

    # 조회수별 정렬
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation'
    )
=======
class Feed(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to="feed_images/", null=True, blank=True)
    video = models.FileField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name="liked_feeds", blank=True)
>>>>>>> b7c59d0 (댓글 생성,수정,삭제 / 피드 생성,수정,삭제)

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
