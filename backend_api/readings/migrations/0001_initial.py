# Generated by Django 5.0.6 on 2024-05-20 15:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 5, 20, 10, 28, 14, 738123))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 5, 20, 10, 28, 14, 738123))),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=100, null=True)),
                ('published_year', models.IntegerField(null=True)),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('publisher', models.CharField(max_length=255, null=True)),
                ('pages', models.IntegerField(null=True)),
                ('language', models.CharField(max_length=50, null=True)),
                ('description', models.TextField(null=True)),
                ('cover_image_url', models.URLField(max_length=255, null=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
