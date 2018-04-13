from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    date =  models.DateField(format=api_settings.DATE_FORMAT)
    time = models.TimeField(format=api_settings.TIME_FORMAT)
    article = models.CharField()
    picture = models.ImageField(allow_empty_file=True)
    url = models.URLFieldmax_length=200, min_length=None, allow_blank=True)

