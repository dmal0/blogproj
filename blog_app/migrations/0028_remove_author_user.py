# Generated by Django 4.2.6 on 2023-11-24 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0027_author_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='user',
        ),
    ]