# Generated by Django 4.0 on 2022-09-24 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work_Orders', '0038_alter_product_product_avrage_prdect_ammount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Product_Code',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='كود العميل'),
        ),
    ]
