# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from web.models import Tag, Poetry, List, Author, Profile

# Register your models here.
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


class PoetryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_name', 'dynasty')


class ListAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Tag, TagAdmin)
admin.site.register(Poetry, PoetryAdmin)
admin.site.register(List, ListAdmin)
admin.site.register(Author)
admin.site.register(Profile)

