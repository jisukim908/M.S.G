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
    image = models.ImageField(blank=True,upload_to="media/photo/%Y/%m/%d", default="static/default_image.jpg")
    
    #video key를 youtube에서 받아와 재생하는 방식으로 변경
    video_key = models.CharField(max_length=20, null=True,help_text="https://www.youtube.com/watch?v= 뒤의 key를 입력하세요")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, default=0, related_name="likes_feed")
    tag = models.ManyToManyField('users.Tag', verbose_name = "tag", blank=False)
    hits = models.PositiveIntegerField(default = 0, verbose_name = "hitcount")

    # 조회수 코드
    @property
    def click(self):
        self.hits +=1
        self.save()

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    feed = models.ForeignKey(Feed, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comment_user"
    )

    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.text