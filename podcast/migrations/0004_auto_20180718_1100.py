# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-18 15:00
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields
import wagtail.wagtailembeds.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0003_auto_20180327_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='soundcloud',
            field=wagtail.wagtailcore.fields.StreamField((('soundcloud_embed', wagtail.wagtailembeds.blocks.EmbedBlock()),)),
        ),
    ]
