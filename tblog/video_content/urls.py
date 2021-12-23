from django.urls import path

from video_content.views import VideoCreateView, display
 


urlpatterns = [
    
    path('upload/',VideoCreateView.as_view(), name='upload'),
    path('videos/',display, name='videos'),
 
]