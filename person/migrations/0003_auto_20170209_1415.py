# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-09 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_auto_20160428_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardandleadershippeoplepage',
            name='former_query',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='person',
            name='former',
            field=models.BooleanField(default=False, help_text=b'Select if person no longer serves above role.'),
        ),
        migrations.AlterField(
            model_name='person',
            name='role',
            field=models.CharField(choices=[(b'Board Member', b'Board Member'), (b'Fellow', b'Fellow'), (b'Central Staff', b'Central Staff'), (b'Program Staff', b'Program Staff'), (b'External Author/Former Staff', b'External Author')], max_length=50),
        ),
    ]
