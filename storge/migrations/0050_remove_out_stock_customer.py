# Generated by Django 4.1.4 on 2023-03-01 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storge', '0049_remove_out_stock_code_out_stock_out_stocknumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='out_stock',
            name='customer',
        ),
    ]
