# Generated by Django 4.0.2 on 2022-03-19 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0005_rename_ad_selection_ads'),
    ]

    operations = [
        migrations.RenameField(
            model_name='selection',
            old_name='ads',
            new_name='items',
        ),
    ]