# Generated by Django 4.0 on 2022-09-26 13:51

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0027_remove_paper_and_cardboard_data_card_total_cut_and_fiber_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='Ord_Binding_Gluing',
        ),
        migrations.AddField(
            model_name='order_states',
            name='orders',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Order.order', verbose_name='الامر'),
        ),
        migrations.AlterField(
            model_name='order',
            name='Ord_Complete_Product',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('باندات', 'باندات'), ('استيك', 'استيك'), ('يدوى', 'يدوى'), ('اخرى', 'اخرى')], max_length=100, null=True, verbose_name='المنتج التام'),
        ),
        migrations.AlterField(
            model_name='order',
            name='Ord_Gluing',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('آلى', 'آلى'), ('يدوى', 'يدوى'), ('تجليد', 'تجليد')], max_length=100, null=True, verbose_name='تلزيق '),
        ),
        migrations.AlterField(
            model_name='order',
            name='Ord_Note_Gluing',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='ملاحظات التلزيق'),
        ),
        migrations.AlterField(
            model_name='order',
            name='Ord_Other_services',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('ورنيش مائى', 'ورنيش مائى'), ('يوفى', 'يوفى'), ('ورنيش دهنى', 'ورنيش دهنى'), ('يوفى ثم ورنيش', 'يوفى ثم ورنيش'), ('سبوت', 'سبوت'), ('اخرى', 'اخرى')], max_length=100, null=True, verbose_name='خدمات اخرى'),
        ),
        migrations.AlterField(
            model_name='order',
            name='Ord_Others',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('كفراج', 'كفراج'), ('تنظيف', 'تنظيف'), ('اخرى', 'اخرى')], max_length=100, null=True, verbose_name='اخرى'),
        ),
        migrations.AlterField(
            model_name='order',
            name='Ord_Packing',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('صناديق', 'صناديق'), ('كرافت/ورق لف', 'كرافت/ورق لف'), ('اكياس', 'اكياس')], max_length=100, null=True, verbose_name='التغليف'),
        ),
        migrations.AlterField(
            model_name='order',
            name='Ord_number_pacu',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='العدد/الباكو'),
        ),
        migrations.AlterField(
            model_name='order',
            name='Ord_number_pandas',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='عدد/الباندات'),
        ),
    ]
