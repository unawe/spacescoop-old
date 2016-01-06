# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('glossary', '0007_auto_20150927_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrytranslation',
            name='title',
            field=models.CharField(verbose_name='title', max_length=50),
        ),
    ]
