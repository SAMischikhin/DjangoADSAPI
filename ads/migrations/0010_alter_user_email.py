# Generated by Django 4.0.2 on 2022-03-28 09:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0009_alter_category_slug_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator(whitelist=['yandex', 'mail', 'list'])]),
        ),
    ]