from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    likes = models.IntegerField(default=0)
    tags = models.CharField(max_length = 50, default = '' )

    def get_absolute_url(self):
        return reverse('blog:post_list')

    def __str__(self):
        return self.title

class Comments(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)

    def get_absolute_url(self):
        return reverse('blog:post_list')