# Generated by Django 5.1.7 on 2025-06-30 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
        migrations.AddField(
            model_name='profile',
            name='mobile',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
