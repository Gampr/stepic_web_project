# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 00:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0002_auto_20160521_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='added_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='added_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]