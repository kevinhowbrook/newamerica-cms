# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-28 18:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_event_programeventspage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='time',
            new_name='start_time',
        ),
        migrations.AddField(
            model_name='event',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='end_time',
            field=models.TimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='address',
            field=models.TextField(default=b'740 15th St NW #900, Washington, DC 20005'),
        ),
        migrations.AlterField(
            model_name='event',
            name='rsvp_link',
            field=models.URLField(default=b'http://www.'),
        ),
    ]
