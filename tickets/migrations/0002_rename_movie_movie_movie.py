# Generated by Django 4.1.7 on 2023-12-12 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='Movie',
            new_name='movie',
        ),
    ]
