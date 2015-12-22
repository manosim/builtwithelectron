# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid
import cloudinary.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.UUIDField(serialize=False, editable=False, default=uuid.uuid4, primary_key=True)),
                ('created', models.DateTimeField(db_index=True, auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('short_description', models.CharField(max_length=255)),
                ('cover', cloudinary.models.CloudinaryField(max_length=255, blank=True, null=True)),
                ('website_url', models.URLField(blank=True, null=True)),
                ('repo_url', models.URLField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('is_featured', models.BooleanField(default=False)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='entries')),
            ],
            options={
                'verbose_name_plural': 'Entries',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.UUIDField(serialize=False, editable=False, default=uuid.uuid4, primary_key=True)),
                ('created', models.DateTimeField(db_index=True, auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.AddField(
            model_name='entry',
            name='tags',
            field=models.ManyToManyField(to='directory.Tag', blank=True, related_name='tags'),
        ),
    ]
