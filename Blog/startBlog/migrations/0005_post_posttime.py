# Generated by Django 5.0.7 on 2024-07-17 14:45

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startBlog', '0004_post_postdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='postTime',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]