from django.urls import path
from channels import views

urlpatterns = [
    path('/<int:user_id>/', views.ChannelsView(), name="channel_view"),
    path('/admin/<int:feed_id>/', views.ChannelAdminView(), name="channel_admin_view"),
]