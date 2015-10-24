# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0002_auto_20151023_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
