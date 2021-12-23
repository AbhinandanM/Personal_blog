from django.db import models

class categories_img(models.Model):
    name            = models.CharField(max_length=120)
    
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')


class Posts(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    category_img = models.CharField(max_length=40, default='')
    preview = models.ImageField(null= True, blank= True)
    time_ago = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class PostImage(models.Model):
    post = models.ForeignKey(Posts, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')

    def __str__(self):
        return self.post.title