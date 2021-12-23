from django.urls import path
from .views import index, post, search, post_update, post_delete, post_create, MessageCreateView, about, AddImg_categoryView, Img_categoryView, Img_categoryListView, MessageUpdateView


urlpatterns = [

    path('', index, name='index'),
    path('search/', search, name='search'),
    path('blog/<title>,<id>/', post, name='post-detail'),
    path('create/', post_create, name='post-create'),
    path('blog/<id>/update/', post_update, name='post-update'),
    path('blog/<id>/delete/', post_delete, name='post-delete'),
    path('create_adm-message/', MessageCreateView.as_view(),
         name='create-adm-message'),
    path('about_us/', about, name='about'),
    path('add_category/', AddImg_categoryView.as_view(), name='add-category'),
    path('category/<str:cates>/', Img_categoryView, name='img_category'),
    path('category-list/', Img_categoryListView, name='img_category-list'),
    path('create_adm-message/update/<int:pk>/',
         MessageUpdateView.as_view(), name='update-adm-message'),

]
