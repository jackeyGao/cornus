# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-22 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_list_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='cover',
            field=models.ImageField(height_field=200, upload_to='cover/%Y/%m/%d/', width_field=200),
        ),
    ]