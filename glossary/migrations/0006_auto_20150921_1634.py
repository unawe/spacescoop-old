# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('glossary', '0005_remove_entrytranslation_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrytranslation',
            name='slug',
            field=models.SlugField(max_length=255, help_text='The Slug must be unique, and closely match the title for better SEO; it is used as part of the URL.', default=''),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='entrytranslation',
            unique_together=set([('language_code', 'master'), ('language_code', 'slug')]),
        ),
    ]
