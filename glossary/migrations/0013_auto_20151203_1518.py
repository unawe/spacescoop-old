# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glossary', '0012_auto_20151021_1709'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ('translations__title',), 'verbose_name_plural': 'entries'},
        ),
    ]
