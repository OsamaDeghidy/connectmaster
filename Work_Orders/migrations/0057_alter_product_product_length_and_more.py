# Generated by Django 4.0 on 2023-08-09 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work_Orders', '0056_alter_product_product_ordered_supply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Product_length',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='Product_width',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
