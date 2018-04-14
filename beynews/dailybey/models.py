from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    date =  models.DateField()
    time = models.TimeField()
    body = models.CharField(max_length=5000)
   # image = models.ImageField(allow_empty_file=True)
    url = models.URLField(max_length=200)

