# Generated by Django 4.0.2 on 2022-03-19 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_selection'),
    ]

    operations = [
        migrations.RenameField(
            model_name='selection',
            old_name='ad',
            new_name='ads',
        ),
    ]
