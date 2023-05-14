from django.urls import path
from feeds import views 

urlpatterns = [
    # home
    path('', views.FeedListView.as_view(), name="feedlist"),
    # feed 생성 / 수정삭제는 channel에서 관리
    path('create_feed/', views.FeedCreateView.as_view(), name="feed_detail"),
    # 개별 feed 상세페이지
    path('<int:feed_id>/', views.FeedDetailView.as_view(), name="feed_detail"),
    # feed like, 좋아요 표시
    path('<int:feed_id>/likes/', views.FeedLikeView.as_view(), name="likes_feed"),
    # comment가져오기
    # path("comments/", views.CommentsView.as_view(), name="comments"),
    # path("comments/<int:comment_id>/", views.CommentsView.as_view(), name="comment_detail"),

    path('comments/<int:feed_id>/', views.CommentsView.as_view(), name="comments"),
    path(
        "comments/<int:comment_id>/like/",
        views.CommentsLikeView.as_view(),
        name="comment_like",
    ),
    path(
        "comments/<int:comment_id>/dislike/",
        views.CommentsDislikeView.as_view(),
        name="comment_dislike",
    ),
    # 피드 검색
    path("search/", views.FeedSearchView.as_view(), name="feed_search"),
]

