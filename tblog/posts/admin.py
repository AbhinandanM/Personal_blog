from django.contrib import admin

from .models import Posts, PostImage, categories_img

class PostImageAdmin(admin.StackedInline):
    model = PostImage

@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
       model = Posts

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(categories_img)