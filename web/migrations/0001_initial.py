# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-12 10:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Poetry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('author', models.CharField(max_length=20)),
                ('dynasty', models.CharField(max_length=20)),
                ('content', models.TextField()),
            ],
            options={
                'db_table': 'poetry',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Category')),
            ],
            options={
                'db_table': 'tag',
            },
        ),
        migrations.AddField(
            model_name='poetry',
            name='tags',
            field=models.ManyToManyField(to='web.Tag'),
        ),
    ]
