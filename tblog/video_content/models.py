from django.db import models
from django.urls import reverse
# Create your models here.

class Videos(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(null= True, blank=True)
    time  = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'
         
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('videos') 