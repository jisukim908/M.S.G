from django.urls import path
from feeds import views 

urlpatterns = [
    path('', views.FeedListView.as_view(), name="feedlist"),
    path('create_feed/', views.FeedCreateView.as_view(), name="feed_detail"),
    path('<int:author_id>/<int:feed_id>/', views.FeedDetailView.as_view(), name="feed_detail"),
    path('<int:author_id>/<int:feed_id>/likes/', views.FeedLikeView.as_view(), name="likes_feed"),
    ### get에는 author_id가 없음.. views.py에 추가함!
    
    path("comments/", views.CommentsView.as_view(), name="comments"),
    path("comments/<int:comment_id>/", views.CommentsView.as_view(), name="comment_detail"),
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
    path("search/", views.FeedSearchView.as_view(), name="feed_search"),
]
