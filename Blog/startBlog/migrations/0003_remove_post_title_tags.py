# Generated by Django 5.1.4 on 2025-01-10 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('startBlog', '0002_post_title_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title_tags',
        ),
    ]
