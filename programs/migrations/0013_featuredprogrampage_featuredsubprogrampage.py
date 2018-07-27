# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-27 17:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('programs', '0012_auto_20180718_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedProgramPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Page')),
                ('program', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='featured_pages', to='programs.Program')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FeaturedSubprogramPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Page')),
                ('program', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='featured_pages', to='programs.Subprogram')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
