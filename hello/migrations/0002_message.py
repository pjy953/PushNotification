# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-16 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('body', models.CharField(max_length=50)),
                ('time', models.DateTimeField()),
            ],
        ),
    ]
