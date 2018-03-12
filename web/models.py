# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'


class Tag(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tag'


class Poetry(models.Model):
    title = models.CharField(max_length=45)
    author = models.CharField(max_length=20)
    dynasty = models.CharField(max_length=20)
    tags = models.ManyToManyField(Tag)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'poetry'
