# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('glossary', '0003_auto_20150921_1522'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entrytranslation',
            options={},
        ),
        migrations.AlterField(
            model_name='entry',
            name='code',
            field=models.SlugField(help_text='The code must be unique, and identical to the english Slug. Do not translate!', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='entrytranslation',
            name='master',
            field=models.ForeignKey(null=True, related_name='translations', to='glossary.Entry'),
        ),
        migrations.AlterModelTable(
            name='entrytranslation',
            table=None,
        ),
    ]
