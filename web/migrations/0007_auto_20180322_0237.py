# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-22 02:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0006_auto_20180320_0725'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick', models.CharField(blank=True, max_length=20, null=True)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('avatar', models.ImageField(upload_to='avatar/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_profile',
            },
        ),
        migrations.AlterField(
            model_name='list',
            name='poetrys',
            field=models.ManyToManyField(blank=True, to='web.Poetry'),
        ),
        migrations.AlterField(
            model_name='poetry',
            name='tags',
            field=models.ManyToManyField(blank=True, to='web.Tag'),
        ),
    ]