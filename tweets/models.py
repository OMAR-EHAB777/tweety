from django.db import models
from django.conf import settings
# Create your models here.
class tweets(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=240)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="tweets")
    likers = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                    related_name="likers")

    def __str__(self):
        return self.content


class comments(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    body = models.TextField()
    tweets = models.ForeignKey(tweets,
                                 on_delete=models.CASCADE,
                                 related_name="comments")
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    voters = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                    related_name="votes")

    def __str__(self):
        return self.author.username