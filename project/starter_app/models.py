from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, primary_key=True)
    created_date = models.DateTimeField(default=timezone.now)
    text = models.TextField()

    def __srt__(self):
        return self.text

    class Meta:
        ordering = ['created_date']
