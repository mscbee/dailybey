from django.db import models


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    date =  models.DateField(auto_now_add=True, blank=True, null=True)
    time = models.TimeField(auto_now_add=True, blank=True, null=True)
    body = models.CharField(max_length=5000, blank=True)
   # image = models.ImageField(allow_empty_file=True)
    url = models.URLField(max_length=200)

    def __str__(self):
        """
        Enables teach object to appear with its title name
        instead of Article object(x)
        """
        return self.title

