# Generated by Django 4.1.4 on 2023-02-11 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storge', '0030_alter_in_stoke_detals_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='slug',
            field=models.SlugField(default='', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
