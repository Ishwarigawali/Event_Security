# Generated by Django 5.0.1 on 2024-02-04 12:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_alter_event_photo_1_alter_event_photo_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='end_time',
            field=models.TimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='event',
            name='start_time',
            field=models.TimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]