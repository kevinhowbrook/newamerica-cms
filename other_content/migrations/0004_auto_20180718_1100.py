# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-18 15:00
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('other_content', '0003_auto_20180424_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otherpost',
            name='attachment',
            field=wagtail.wagtailcore.fields.StreamField((('attachment', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=False)),), null=True),
        ),
    ]
