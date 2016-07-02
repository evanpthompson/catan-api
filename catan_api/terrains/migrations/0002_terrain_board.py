# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-30 22:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
        ('terrains', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='terrain',
            name='board',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='boards.Board'),
            preserve_default=False,
        ),
    ]
