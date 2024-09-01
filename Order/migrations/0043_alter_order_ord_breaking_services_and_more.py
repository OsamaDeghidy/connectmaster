# Generated by Django 4.2.9 on 2024-03-28 07:12

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0042_alter_order_states_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Ord_Breaking_services',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('', ''), ('فورمه جديد', 'فورمه جديد'), ('فورمه قديمه', 'فورمه قديمه')], max_length=100, null=True, verbose_name='خدمات التكسير'),
        ),
        migrations.AlterField(
            model_name='order',
            name='Ord_Complete_Product',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('', ''), ('باندات', 'باندات'), ('استيك', 'استيك'), ('يدوى', 'يدوى'), ('اخرى', 'اخرى')], max_length=100, null=True, verbose_name='المنتج التام'),
        ),
        migrations.AlterField(
            model_name='order',
            name='Ord_Gluing',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('', ''), ('آلى', 'آلى'), ('يدوى', 'يدوى'), ('تجليد', 'تجليد')], max_length=100, null=True, verbose_name='تلزيق '),
        ),
        migrations.AlterField(
            model_name='order',
            name='Ord_Operation_type',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('', ''), ('مكررة', 'مكررة'), ('جديدة', 'جديدة'), ('تعديل', 'تعديل')], max_length=50, null=True, verbose_name='نوع العملية'),
        ),
        migrations.AlterField(
            model_name='order',
            name='Ord_Other_services',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('', ''), ('ورنيش مائى', 'ورنيش مائى'), ('يوفى', 'يوفى'), ('ورنيش دهنى', 'ورنيش دهنى'), ('يوفى ثم ورنيش', 'يوفى ثم ورنيش'), ('سبوت', 'سبوت'), ('اخرى', 'اخرى')], max_length=100, null=True, verbose_name='خدمات اخرى'),
        ),
        migrations.AlterField(
            model_name='order',
            name='Ord_Packing',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('', ''), ('صناديق', 'صناديق'), ('كرافت/ورق لف', 'كرافت/ورق لف'), ('اكياس', 'اكياس')], max_length=100, null=True, verbose_name='التغليف'),
        ),
        migrations.AlterField(
            model_name='order',
            name='Ord_type_print',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('', ''), ('ربع', 'ربع'), ('نص', 'نص'), ('فرخ', 'فرخ')], max_length=50, null=True, verbose_name=' الطباعة'),
        ),
    ]
