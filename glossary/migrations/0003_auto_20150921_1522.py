# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('glossary', '0002_auto_20150917_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='code',
            field=models.SlugField(unique=True, max_length=255, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entrytranslation',
            name='short_description',
            field=models.CharField(max_length=160),
        ),
    ]
