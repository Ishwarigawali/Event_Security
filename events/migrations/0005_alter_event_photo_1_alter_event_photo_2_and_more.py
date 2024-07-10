# Generated by Django 5.0.1 on 2024-02-03 18:24

import events.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_alter_event_photo_1_alter_event_photo_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='photo_1',
            field=models.ImageField(blank=True, upload_to=events.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='event',
            name='photo_2',
            field=models.ImageField(blank=True, upload_to=events.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='event',
            name='photo_3',
            field=models.ImageField(blank=True, upload_to=events.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='event',
            name='photo_main',
            field=models.ImageField(upload_to=events.models.user_directory_path),
        ),
    ]
