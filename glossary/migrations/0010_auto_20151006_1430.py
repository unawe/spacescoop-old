# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('glossary', '0009_auto_20150928_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrytranslation',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='entrytranslation',
            name='short_description',
            field=models.CharField(max_length=180),
        ),
    ]
