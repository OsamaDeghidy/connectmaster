# Generated by Django 4.1.4 on 2023-03-22 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storge', '0052_remove_out_stock_total_sheet_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='in_stock',
            name='total_sheet',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='إجمالي الشيت'),
        ),
        migrations.AddField(
            model_name='in_stock',
            name='total_weight',
            field=models.FloatField(blank=True, default=0, max_length=100, null=True, verbose_name='إجمالي الوزن'),
        ),
        migrations.AlterField(
            model_name='in_stock',
            name='price',
            field=models.FloatField(blank=True, default=0, max_length=100, null=True, verbose_name='السعر'),
        ),
        migrations.AlterField(
            model_name='out_stock',
            name='price',
            field=models.FloatField(blank=True, default=0, max_length=100, null=True, verbose_name='السعر'),
        ),
    ]
