# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-20 07:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_poetry_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='poetrys',
            field=models.ManyToManyField(blank=True, null=True, to='web.Poetry'),
        ),
        migrations.AlterField(
            model_name='poetry',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='web.Tag'),
        ),
    ]
