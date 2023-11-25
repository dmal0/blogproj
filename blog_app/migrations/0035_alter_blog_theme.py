# Generated by Django 4.2.6 on 2023-11-24 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0034_alter_blog_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='theme',
            field=models.CharField(choices=[('None', 'None'), ('BO', 'Blood Orange'), ('LL', 'Lemon Lime')], default=None, max_length=200, null=True),
        ),
    ]