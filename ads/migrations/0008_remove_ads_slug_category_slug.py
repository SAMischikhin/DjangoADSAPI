# Generated by Django 4.0.2 on 2022-03-28 09:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0007_ads_slug_user_birth_date_alter_ads_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ads',
            name='slug',
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(default=1, max_length=10, validators=[django.core.validators.MinLengthValidator(5, 'the field must contain at least 5 characters')]),
            preserve_default=False,
        ),
    ]
