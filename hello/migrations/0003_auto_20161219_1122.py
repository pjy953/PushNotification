# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-19 02:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registrationid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regid', models.CharField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
