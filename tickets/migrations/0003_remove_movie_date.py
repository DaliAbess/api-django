# Generated by Django 4.2.8 on 2023-12-13 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_rename_movie_movie_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='date',
        ),
    ]
