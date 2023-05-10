from django.urls import path
from channels import views

urlpatterns = [
    path('<int:user_id>/info/', views.ChannelinfoView.as_view(), name="channel_info_view"),
    path('<int:user_id>/', views.ChannelsView.as_view(), name="channel_view"),
    path('admin/<int:user_id>/<int:feed_id>/', views.ChannelAdminView.as_view(), name="channel_admin_view"),
]