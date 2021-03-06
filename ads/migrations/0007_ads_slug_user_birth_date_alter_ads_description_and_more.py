# Generated by Django 4.0.2 on 2022-03-28 09:29

import ads.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0006_rename_ads_selection_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='slug',
            field=models.CharField(default='2000-02-02', max_length=10, validators=[django.core.validators.MinLengthValidator(5, 'the field must contain at least 5 characters')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='birth_date',
            field=models.DateField(default='2000-02-02', validators=[ads.models.under_nine]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ads',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='ads',
            name='name',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(10, 'the field must contain at least 10 characters')]),
        ),
        migrations.AlterField(
            model_name='ads',
            name='price',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
