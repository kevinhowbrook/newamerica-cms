# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-03-27 21:18
from __future__ import unicode_literals

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0004_auto_20180226_0804'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='allreportshomepage',
            options={'verbose_name': 'Reports Homepage'},
        ),
        migrations.AlterField(
            model_name='report',
            name='sections',
            field=wagtail.wagtailcore.fields.StreamField([(b'section', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.TextBlock()), (b'body', wagtail.wagtailcore.blocks.StreamBlock([(b'introduction', wagtail.wagtailcore.blocks.RichTextBlock(icon=b'openquote')), (b'heading', wagtail.wagtailcore.blocks.CharBlock(classname=b'full title', icon=b'title', template=b'blocks/heading.html')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), (b'inline_image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image', required=True)), (b'align', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'center', b'Centered'), (b'left', b'Left'), (b'right', b'Right')], default=b'centered')), (b'width', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'initial', b'Auto'), (b'width-133', b'Medium'), (b'width-166', b'Large'), (b'width-200', b'X-Large')], default=b'initial')), (b'figure_number', wagtail.wagtailcore.blocks.CharBlock(max_length=3, required=False)), (b'figure_title', wagtail.wagtailcore.blocks.CharBlock(max_length=100, required=False)), (b'open_image_on_click', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False))], icon=b'image')), (b'video', wagtail.wagtailembeds.blocks.EmbedBlock(icon=b'media')), (b'table', wagtail.contrib.table_block.blocks.TableBlock()), (b'button', wagtail.wagtailcore.blocks.StructBlock([(b'button_text', wagtail.wagtailcore.blocks.CharBlock(max_length=50, required=True)), (b'button_link', wagtail.wagtailcore.blocks.URLBlock(default=b'https://www.', required=True)), (b'alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'left-aligned', b'Left'), (b'center-aligned', b'Center')]))])), (b'iframe', wagtail.wagtailcore.blocks.StructBlock([(b'source_url', wagtail.wagtailcore.blocks.URLBlock(required=True)), (b'width', wagtail.wagtailcore.blocks.IntegerBlock(help_text=b'The maximum possible iframe width is 1050', max_value=1050)), (b'height', wagtail.wagtailcore.blocks.IntegerBlock())], icon=b'link')), (b'dataviz', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'subheading', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'max_width', wagtail.wagtailcore.blocks.IntegerBlock()), (b'show_chart_buttons', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False)), (b'container_id', wagtail.wagtailcore.blocks.CharBlock(required=True))], icon=b'code')), (b'timeline', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'subheading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'default_view', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'timeline', b'Timeline'), (b'list', b'List')], default=b'timeline', help_text=b'Should the default view be a timeline or a list?', required=False)), (b'major_timeline_splits', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'start_date', wagtail.wagtailcore.blocks.DateBlock(required=True)), (b'end_date', wagtail.wagtailcore.blocks.DateBlock(required=False)), (b'date_display_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'year', b'Year'), (b'month', b'Month'), (b'day', b'Day')], default=b'year', help_text=b'Controls how specific the date is displayed'))]), default=b'', required=False)), (b'event_eras', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'start_date', wagtail.wagtailcore.blocks.DateBlock(required=True)), (b'end_date', wagtail.wagtailcore.blocks.DateBlock(required=False)), (b'date_display_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'year', b'Year'), (b'month', b'Month'), (b'day', b'Day')], default=b'year', help_text=b'Controls how specific the date is displayed'))]), default=b'', required=False)), (b'event_categories', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock(), default=b'', required=False)), (b'event_list', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'italicize_title', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False)), (b'description', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'category', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'start_date', wagtail.wagtailcore.blocks.DateBlock(required=True)), (b'end_date', wagtail.wagtailcore.blocks.DateBlock(required=False)), (b'date_display_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'year', b'Year'), (b'month', b'Month'), (b'day', b'Day')], default=b'year', help_text=b'Controls how specific the date is displayed'))])))], icon=b'arrows-up-down')), (b'google_map', wagtail.wagtailcore.blocks.StructBlock([(b'use_page_address', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text=b'If selected, map will use the address already defined for this page, if applicable. For most posts besides events, this should be left unchecked and the form below should be completed.', required=False)), (b'street', wagtail.wagtailcore.blocks.TextBlock(required=False)), (b'city', wagtail.wagtailcore.blocks.TextBlock(default=b'Washington', required=False)), (b'state', wagtail.wagtailcore.blocks.TextBlock(default=b'D.C.', required=False)), (b'zipcode', wagtail.wagtailcore.blocks.TextBlock(default=b'200', required=False))], icon=b'site')), (b'resource_kit', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'description', wagtail.wagtailcore.blocks.TextBlock(required=False)), (b'resources', wagtail.wagtailcore.blocks.StreamBlock([(b'post', wagtail.wagtailcore.blocks.StructBlock([(b'name', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image', required=False)), (b'description', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'resource', wagtail.wagtailcore.blocks.PageChooserBlock(required=True))], icon=b'redirect', label=b'Post')), (b'external_resource', wagtail.wagtailcore.blocks.StructBlock([(b'name', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image', required=False)), (b'description', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'resource', wagtail.wagtailcore.blocks.URLBlock(required=True))], icon=b'site', label=b'External resource')), (b'attachment', wagtail.wagtailcore.blocks.StructBlock([(b'name', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image', required=False)), (b'description', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'resource', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=True))], icon=b'doc-full', label=b'Attachment'))]))], icon=b'folder'))]))], template=b'components/report_section_body.html'))]),
        ),
    ]
