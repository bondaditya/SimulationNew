# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-27 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marketing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offline', models.PositiveIntegerField(default=0)),
                ('online', models.PositiveIntegerField(default=0)),
                ('tv', models.PositiveIntegerField(default=0)),
                ('radio', models.PositiveIntegerField(default=0)),
                ('prints', models.PositiveIntegerField(default=0)),
                ('hr', models.PositiveIntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
