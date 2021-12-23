from django.contrib import admin

# Register your models here.
from .models import Author, Category, Post, Comment, PostViewCount, AdmMessage, img_categories

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostViewCount)
admin.site.register(AdmMessage)
admin.site.register(img_categories)
