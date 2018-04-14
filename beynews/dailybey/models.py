from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    date =  models.DateField(auto_now_add=True, blank=True, null=True)
    time = models.TimeField(auto_now_add=True, blank=True, null=True)
    body = models.CharField(max_length=5000)
   # image = models.ImageField(allow_empty_file=True)
    url = models.URLField(max_length=200)

