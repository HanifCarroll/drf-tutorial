# Generated by Django 4.1.6 on 2023-02-05 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='code',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]