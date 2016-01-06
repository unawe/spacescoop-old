# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glossary', '0010_auto_20151006_1430'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['translations__title'], 'verbose_name_plural': 'entries'},
        ),
    ]
