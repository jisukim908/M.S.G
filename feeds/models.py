from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCountMixin, HitCount
from django.conf import settings
from django.contrib.auth import get_user_model


class Feed(models.Model, HitCountMixin):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="author"
    )
    title = models.CharField(max_length=100)
    context = models.TextField(blank=True)
    image = models.ImageField(blank=True,upload_to="media/photo/%Y/%m/%d", default="defalut_image.jpg")
    
    #video key를 youtube에서 받아와 재생하는 방식으로 변경
    video_key = models.CharField(max_length=20, help_text="https://www.youtube.com/watch?v= 뒤의 key를 입력하세요")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, default=0, related_name="likes_feed")
    

    # 조회수별 정렬
    hit_count_generic = GenericRelation(
        HitCount,
        object_id_field="object_pk",
        related_query_name="hit_count_generic_relation",
    )

    def __str__(self):
        return self.title
    

User = get_user_model()

class Comment(models.Model):
    feed = models.ForeignKey(Feed, related_name="comments", on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.text
