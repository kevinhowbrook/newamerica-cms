# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-30 15:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20160328_1935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='address',
        ),
        migrations.AddField(
            model_name='event',
            name='city',
            field=models.TextField(default=b'Washington'),
        ),
        migrations.AddField(
            model_name='event',
            name='host_organization',
            field=models.TextField(blank=True, default=b'New America', null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='state',
            field=models.TextField(default=b'D.C.'),
        ),
        migrations.AddField(
            model_name='event',
            name='street_address',
            field=models.TextField(default=b'740 15th St NW #900'),
        ),
        migrations.AddField(
            model_name='event',
            name='zipcode',
            field=models.TextField(default=b'20005'),
        ),
    ]