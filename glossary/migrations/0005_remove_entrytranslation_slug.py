# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('glossary', '0004_auto_20150921_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrytranslation',
            name='slug',
        ),
    ]
