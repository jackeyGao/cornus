# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from collections import defaultdict
from django.shortcuts import render_to_response
from web.models import Tag, Poetry

BRS = ('？', '。', '！')

# Create your views here.
def index(request):
    tags = Tag.objects.all()
    return render_to_response('index.html', locals())


def list_view(request, tag_name):
    tag = Tag.objects.filter(name=tag_name).first()
    poetrys = Poetry.objects.filter(tags__in=[tag])

    for i in poetrys:
        i.content = i.content.replace('？', '？\n')
        i.content = i.content.replace('。', '。\n')
        i.content = i.content.replace('！', '！\n')

    return render_to_response('list.html', locals())
    

def test(request):
    tags = Tag.objects.all()
    return render_to_response('test.html', locals())
    
