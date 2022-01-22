from django.db import models


class Article(models.Model):
    content = models.TextField(blank=False, default="")
    date = models.DateField()
