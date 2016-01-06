# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('glossary', '0006_auto_20150921_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='code',
        ),
        migrations.AlterField(
            model_name='entrytranslation',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, populate_from='title', editable=False, unique_with=('language_code',)),
        ),
    ]
