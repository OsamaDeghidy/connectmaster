# Generated by Django 4.0 on 2022-09-20 10:41

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Work_Orders', '0034_alter_design_and_printing_specifications_pro_design_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aftar_print_services',
            name='pro_aftar_print_services_type',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('قص', 'قص'), ('ورنيش ', 'ورنيش '), ('يوفى', 'يوفى'), ('سلوفان', 'سلوفان'), ('سبوت يوفى', 'سبوت يوفى'), ('بصمه', 'بصمه'), ('مضلع', 'مضلع')], default=None, max_length=100, null=True, verbose_name='نوع الخدمه '),
        ),
    ]
