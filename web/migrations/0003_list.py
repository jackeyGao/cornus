# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-19 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20180314_0304'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('cover', models.ImageField(upload_to='cover/%Y/%m/%d/')),
                ('poetrys', models.ManyToManyField(to='web.Poetry')),
            ],
            options={
                'db_table': 'list',
            },
        ),
    ]
