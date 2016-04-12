# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-28 17:53
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_programblogpostspage'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='attachment',
            field=wagtail.wagtailcore.fields.StreamField([(b'attachment', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=False))], null=True),
        ),
        migrations.AddField(
            model_name='programblogpostspage',
            name='subheading',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, null=True),
        ),
    ]