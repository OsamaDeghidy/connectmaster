# Generated by Django 4.0 on 2022-09-26 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work_Orders', '0039_alter_product_product_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Product_Code',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='كود العميل'),
        ),
    ]
