# Generated by Django 4.2.6 on 2023-11-25 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0036_alter_blog_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='theme',
            field=models.CharField(choices=[('None', 'None'), ('BO', 'Blood Orange'), ('LL', 'Lemon Lime'), ('UH', 'Ube Halaya'), ('Dark', 'Dark')], default=None, max_length=200, null=True),
        ),
    ]
