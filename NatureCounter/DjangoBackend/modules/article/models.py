from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.


class ArticleCategory(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category


class Article(models.Model):
    title = models.CharField(max_length=200, unique=True, null=False)
    subTitle = models.CharField(max_length=200)
    category = models.ForeignKey(
        ArticleCategory, on_delete=models.CASCADE, null=False)
    readTime = models.IntegerField(default=0)
    description = RichTextField()
    image = models.CharField(max_length=200)
    featured = models.BooleanField(default=False)
    createdBy = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    createdDateTime = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title
