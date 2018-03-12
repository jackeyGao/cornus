# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from web.models import Category, Tag, Poetry

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('category', 'name',)


class PoetryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'dynasty')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Poetry, PoetryAdmin)

