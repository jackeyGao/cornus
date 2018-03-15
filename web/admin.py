# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from web.models import Tag, Poetry

# Register your models here.
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


class PoetryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'dynasty')


admin.site.register(Tag, TagAdmin)
admin.site.register(Poetry, PoetryAdmin)

