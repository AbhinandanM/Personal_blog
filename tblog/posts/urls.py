from django.urls import path
from posts.views import img_view, detail_view, create_post_view


urlpatterns = [

    path('gallery/', img_view, name='gallery'),
    path('create-post/', create_post_view, name='create-post'),
    path('gallery/<int:id>/', detail_view, name='detail'),
]

