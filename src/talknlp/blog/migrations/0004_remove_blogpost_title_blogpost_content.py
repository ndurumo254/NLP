# Generated by Django 5.0.9 on 2024-09-28 13:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_blogpost_can_delete"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blogpost",
            name="title",
        ),
        migrations.AddField(
            model_name="blogpost",
            name="content",
            field=models.TextField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
