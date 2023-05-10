from django.urls import path
from feeds import views

urlpatterns = [
    path('', views.FeedListView.as_view(), name="feedlist"),
    path('create_feed/', views.FeedCreateView.as_view(), name="feed_detail"),
    path('<int:author_id>/<int:feed_id>/', views.FeedDetailView.as_view(), name="feed_detail"),
    path('<int:author_id>/<int:feed_id>/likes/', views.LikeView.as_view(), name="likes_feed"),
]