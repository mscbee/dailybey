from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    date =  models.DateField()
    time = models.TimeField()
    article = models.CharField(max_length=5000)
   # picture = models.ImageField(allow_empty_file=True)
    url = models.URLField(max_length=200)

