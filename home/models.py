from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300)

    def __str__(self):
        return self.title
