from django.urls import path
from App_Posts import views

app_name='app_post'
urlpatterns = [
    path('upload/',views.upload,name='upload'),
    path('details/<pk>/',views.video,name='details'),
    path('edit_post/<pk>/',views.edit_post,name='edit_post'),
    path('delete_post/<pk>/',views.DeletePost.as_view(),name='delete_post'),
    path('user_video/',views.user_video,name='user_video'),
    path('delete_video/<pk>/',views.DeleteVideo.as_view(),name='delete_video'),
]
