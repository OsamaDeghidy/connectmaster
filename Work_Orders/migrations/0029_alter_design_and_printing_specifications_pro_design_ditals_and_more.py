# Generated by Django 4.0.2 on 2022-07-16 09:03

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Work_Orders', '0028_alter_customer_customer_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design_and_printing_specifications',
            name='pro_design_ditals',
            field=models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='تفاصيل التصميم '),
        ),
        migrations.AlterField(
            model_name='design_and_printing_specifications',
            name='pro_old_execution',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('اعدام القديم  ', 'اعدام القديم  ')], default=None, max_length=70, null=True, verbose_name=''),
        ),
    ]
