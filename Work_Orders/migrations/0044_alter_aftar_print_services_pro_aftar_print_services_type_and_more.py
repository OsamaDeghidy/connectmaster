# Generated by Django 4.0 on 2022-10-06 13:34

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Work_Orders', '0043_alter_design_and_printing_specifications_number_of_sides_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aftar_print_services',
            name='pro_aftar_print_services_type',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('قص', 'قص'), ('ورنيش ', 'ورنيش '), ('يوفى', 'يوفى'), ('سلوفان', 'سلوفان'), ('سبوت يوفى', 'سبوت يوفى'), ('بصمه', 'بصمه'), ('مضلع', 'مضلع')], default=None, max_length=100, null=True, verbose_name='نوع الخدمة'),
        ),
        migrations.AlterField(
            model_name='crushing_data',
            name='pro_crushing_data_type',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('تام', 'تام'), ('شباك', 'شباك'), ('كوفراج', 'كوفراج'), ('ريجة', 'ريجة'), ('فورمة', 'فورمة')], max_length=100, null=True, verbose_name='نوع الخدمة '),
        ),
        migrations.AlterField(
            model_name='design_and_printing_specifications',
            name='attachments_file',
            field=models.FileField(blank=True, null=True, upload_to='attachments/%Y/%m/%d', verbose_name='إرفاق ملف معتمد  '),
        ),
        migrations.AlterField(
            model_name='design_and_printing_specifications',
            name='product_color',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Cyan', 'C'), ('Magenta', 'M'), ('yellow', 'Y'), ('Key', 'K')], default=None, max_length=50, null=True, verbose_name='الألون'),
        ),
        migrations.AlterField(
            model_name='gluing_and_binding_data',
            name='pro_Gluing_And_Binding_Data_type',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('تلزيق آلى', 'تلزيق آلى'), ('تلزيق يدوى', 'تلزيق يدوى'), ('تلزيق استالون', 'تلزيق استالون'), ('تجليد', 'تجليد')], max_length=100, null=True, verbose_name='نوع الخدمة '),
        ),
        migrations.AlterField(
            model_name='paper_specification',
            name='fiber_direction',
            field=models.CharField(blank=True, choices=[('ضرورية', 'ضرورية'), ('غير ضرورىة', 'غير ضرورىة')], default=None, max_length=80, null=True, verbose_name='إتجاه الألياف '),
        ),
        migrations.AlterField(
            model_name='product',
            name='Product_Allowable_increase',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('حسب امر الشغل', 'حسب امر الشغل'), ('10% بحد اقصى', '10% بحد اقصى')], default='حسب امر الشغل ', max_length=50, verbose_name='*الزيادة المسموح بها  '),
        ),
        migrations.AlterField(
            model_name='product',
            name='customer_representative',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('د/عمروالباز', 'د/عمروالباز'), ('ا/عمرو احمد', 'ا/عمرو احمد'), ('م/كريم عبد الغنى', 'م/كريم عبد الغنى'), ('أخرى', 'أخرى')], max_length=100, verbose_name='ممثل  العميل'),
        ),
    ]
