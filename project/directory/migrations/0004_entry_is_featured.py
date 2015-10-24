# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0003_entry_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
