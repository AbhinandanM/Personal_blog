from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username


class PostViewCount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class AdmMessage(models.Model):
    title = models.CharField(max_length=40)
    title_tag = RichTextField()
    timestamps = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('index')


class img_categories(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')


class Post(models.Model):
    title = models.CharField(max_length=120)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = RichTextUploadingField()
    date_added = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    thumbnail = models.ImageField()
    featured = models.BooleanField()
    previous_post = models.ForeignKey(
        'self', related_name='previous', on_delete=models.SET_NULL, null=True, blank=True)
    next_post = models.ForeignKey(
        'self', related_name='next', on_delete=models.SET_NULL, null=True, blank=True)
    img_category = models.CharField(max_length=40, default='')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'id': self.id, 'title': self.title})

    def get_update_url(self):
        return reverse('post-update', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('post-delete', kwargs={'id': self.id})

    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')

    # @property
    # def comment_count(self):
        # return Comment.objects.filter(post=self).count()

    @property
    def view_count(self):
        return PostViewCount.objects.filter(post=self).count()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
