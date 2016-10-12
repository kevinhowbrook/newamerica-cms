# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-12 17:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import home.blocks
import wagtail.contrib.table_block.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('in_depth', '0006_auto_20160926_1310'),
    ]

    operations = [
        migrations.CreateModel(
            name='InDepthProfile',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('subheading', wagtail.wagtailcore.fields.RichTextField(blank=True, null=True)),
                ('lookup_field', models.CharField(help_text='The name of the field where the query value will be found', max_length=150)),
                ('body', wagtail.wagtailcore.fields.StreamField([('introduction', wagtail.wagtailcore.blocks.RichTextBlock()), ('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('video', wagtail.wagtailembeds.blocks.EmbedBlock(icon='media')), ('table', wagtail.contrib.table_block.blocks.TableBlock()), ('button', wagtail.wagtailcore.blocks.StructBlock([(b'button_text', wagtail.wagtailcore.blocks.CharBlock(max_length=50, required=True)), (b'button_link', wagtail.wagtailcore.blocks.URLBlock(default=b'https://www.', required=True)), (b'alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'left-aligned', b'Left'), (b'center-aligned', b'Center')]))])), ('iframe', wagtail.wagtailcore.blocks.StructBlock([(b'source_url', wagtail.wagtailcore.blocks.URLBlock(required=True)), (b'width', home.blocks.IntegerBlock(help_text=b'The maximum possible iframe width is 1050', max_value=1050)), (b'height', home.blocks.IntegerBlock())])), ('dataviz', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'subheading', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'max_width', home.blocks.IntegerBlock()), (b'show_download_link', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False)), (b'container_id', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('collapsible', wagtail.wagtailcore.blocks.StructBlock([(b'hidden_by_default', wagtail.wagtailcore.blocks.StreamBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(classname=b'full title')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image')), (b'video', wagtail.wagtailembeds.blocks.EmbedBlock(icon=b'media')), (b'table', wagtail.contrib.table_block.blocks.TableBlock()), (b'button', wagtail.wagtailcore.blocks.StructBlock([(b'button_text', wagtail.wagtailcore.blocks.CharBlock(max_length=50, required=True)), (b'button_link', wagtail.wagtailcore.blocks.URLBlock(default=b'https://www.', required=True)), (b'alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'left-aligned', b'Left'), (b'center-aligned', b'Center')]))])), (b'iframe', wagtail.wagtailcore.blocks.StructBlock([(b'source_url', wagtail.wagtailcore.blocks.URLBlock(required=True)), (b'width', home.blocks.IntegerBlock(help_text=b'The maximum possible iframe width is 1050', max_value=1050)), (b'height', home.blocks.IntegerBlock())])), (b'dataviz', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'subheading', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'max_width', home.blocks.IntegerBlock()), (b'show_download_link', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False)), (b'container_id', wagtail.wagtailcore.blocks.CharBlock(required=True))]))]))])), ('data_reference', wagtail.wagtailcore.blocks.StructBlock([(b'display_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'in-text', b'In-Text'), (b'fact-box', b'Fact-Box'), (b'list', b'List')])), (b'display_fields', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'field_name', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'format', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'date', b'Date'), (b'list', b'List'), (b'number', b'Number(with thousands-place comma)'), (b'percent', b'Percent'), (b'plain_text', b'Plain-text'), (b'price', b'Price'), (b'rank', b'Rank')]))])))]))])),
                ('data_profile_external_script', models.CharField(blank=True, help_text='Specify the name of the external script file within the na-data-projects/projects AWS directory to include that script in the body of the document.', max_length=140, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
