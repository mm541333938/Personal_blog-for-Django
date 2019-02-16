from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    """分类"""
    name = models.CharField(max_length=100)


class Tag(models.Model):
    """标签"""
    name = models.CharField(max_length=100)


class Post(models.Model):
    """文章"""
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=True)  # 一对多的关系, 指定外键的时候需要对on_delete= True  or = models.CASCADE
    tags = models.ManyToManyField(Tag, blank=True)  # 多对多的关系
    author = models.ForeignKey(User, on_delete=True)
