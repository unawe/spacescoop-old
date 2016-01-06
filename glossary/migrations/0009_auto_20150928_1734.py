# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('glossary', '0008_auto_20150928_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrytranslation',
            name='title',
            field=models.CharField(max_length=200, verbose_name='title'),
        ),
    ]
