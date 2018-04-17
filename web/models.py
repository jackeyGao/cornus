# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nick = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='avatar/')

    class Meta:
        db_table = "user_profile"
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tag'


class Author(models.Model):
    name = models.CharField(max_length=20)
    intro = models.TextField()
    avatar = models.ImageField(upload_to='author_avatar/')
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'author'


class Poetry(models.Model):
    title = models.CharField(max_length=45)
    author_name = models.CharField(max_length=20)
    author = models.ForeignKey(Author)
    dynasty = models.CharField(max_length=20)
    tags = models.ManyToManyField(Tag, blank=True)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'poetry'


class List(models.Model):
    name = models.CharField(max_length=25)
    intro = models.TextField()
    owner = models.ForeignKey(User)
    cover = models.ImageField(upload_to='cover/%Y/%m/%d/')
    poetrys =  models.ManyToManyField(Poetry, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'list'

