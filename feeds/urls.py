from django.urls import path
from .views import (
    FeedListView,
    FeedDetailView,
    FeedCreateView,
    CommentsView,
    CommentsLikeView,
    CommentsDislikeView,
)

urlpatterns = [
    path("feedlist/", FeedListView.as_view(), name="feed_list"),
    path("feed/<int:post_id>/", FeedDetailView.as_view(), name="feed_detail"),
    path("feed/create/", FeedCreateView.as_view(), name="feed_create"),
    path("feed/<int:post_id>/update/", FeedCreateView.as_view(), name="feed_update"),
    path("feed/<int:post_id>/delete/", FeedCreateView.as_view(), name="feed_delete"),
    path("comments/", CommentsView.as_view(), name="comments"),
    path("comments/<int:comment_id>/", CommentsView.as_view(), name="comment_detail"),
    path(
        "comments/<int:comment_id>/like/",
        CommentsLikeView.as_view(),
        name="comment_like",
    ),
    path(
        "comments/<int:comment_id>/dislike/",
        CommentsDislikeView.as_view(),
        name="comment_dislike",
    ),
]
