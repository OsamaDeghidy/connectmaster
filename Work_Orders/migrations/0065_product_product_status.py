# Generated by Django 4.0 on 2023-09-16 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work_Orders', '0064_alter_product_customer_representative'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Product_status',
            field=models.CharField(blank=True, choices=[('Active', 'Active'), ('Deleted', 'Deleted')], default='Active', max_length=50, null=True),
        ),
    ]
