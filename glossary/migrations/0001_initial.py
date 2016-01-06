# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EntryTranslation',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('language_code', models.CharField(verbose_name='Language', db_index=True, max_length=15)),
                ('slug', models.SlugField(unique=True, help_text='The Slug must be unique, and closely match the title for better SEO; it is used as part of the URL.', max_length=255)),
                ('title', models.CharField(verbose_name='title', max_length=255)),
                ('short_description', models.CharField(verbose_name='short description', max_length=160)),
                ('description', ckeditor.fields.RichTextField(blank=True)),
                ('master', models.ForeignKey(null=True, related_name='translations', to='glossary.Entry', editable=False)),
            ],
            options={
                'db_tablespace': '',
                'default_permissions': (),
                'verbose_name': 'entry Translation',
                'db_table': 'glossary_entry_translation',
                'managed': True,
            },
        ),
        migrations.AlterUniqueTogether(
            name='entrytranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
