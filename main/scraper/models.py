from re import A
from django.db import models


class Article(models.Model):
    title = models.TextField(blank=False, default="")
    content = models.TextField(blank=False, default="")
    date = models.DateTimeField(auto_now_add=True)
