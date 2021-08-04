from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=120, default='')
    description = models.TextField()

    def __str__(self):
        return self.title
