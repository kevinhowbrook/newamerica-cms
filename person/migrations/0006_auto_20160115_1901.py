# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-15 19:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0003_auto_20160106_2229'),
        ('person', '0005_auto_20160106_2246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='program',
        ),
        migrations.AddField(
            model_name='person',
            name='belongs_to_program',
            field=models.ForeignKey(blank=True, help_text=b'The Program this person works for', null=True, on_delete=django.db.models.deletion.CASCADE, to='programs.Program'),
        ),
    ]