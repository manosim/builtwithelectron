# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name_plural': 'Entries'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name_plural': 'Tags'},
        ),
        migrations.AlterField(
            model_name='entry',
            name='tags',
            field=models.ManyToManyField(to='directory.Tag', related_name='tags', blank=True),
        ),
    ]
