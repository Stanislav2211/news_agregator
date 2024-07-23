from django.db import models

class BBC(models.Model):
    title = models.CharField(max_length=255)
    article = models.TextField()
    url = models.URLField()

    class Meta:
        verbose_name_plural = 'BBC'

class HackerNews(models.Model):
    title = models.CharField(max_length=255)
    points = models.CharField()
    author = models.CharField(max_length=255)
    url = models.URLField()

    class Meta:
        verbose_name_plural = 'HackerNews'