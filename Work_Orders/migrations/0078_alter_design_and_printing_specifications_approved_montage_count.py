# Generated by Django 4.2.9 on 2024-07-24 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work_Orders', '0077_alter_product_customer_representative'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design_and_printing_specifications',
            name='approved_montage_count',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='العدد في المونتاج المعتمد'),
        ),
    ]
