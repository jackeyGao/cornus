# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from collections import defaultdict
from django.shortcuts import render_to_response
from web.models import Category, Tag, Poetry

# Create your views here.

def index(request):
    categorys = defaultdict(list)

    for x in Tag.objects.all():
        categorys[x.category].append(x.name)
    categorys = dict(categorys)

    return render_to_response('index.html', locals())
