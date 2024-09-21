# Generated by Django 4.1.4 on 2023-02-16 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storge', '0036_remove_customer_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='out_stock',
            name='In_stock',
        ),
        migrations.RemoveField(
            model_name='out_stock',
            name='iteam',
        ),
        migrations.RemoveField(
            model_name='out_stock',
            name='quntity',
        ),
        migrations.AddField(
            model_name='out_stock',
            name='code',
            field=models.CharField(default=1, max_length=100, verbose_name='الكود'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='out_stock',
            name='in_stock_detals',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='storge.in_stoke_detals'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='out_stock',
            name='sheet',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='out_stock',
            name='weaight',
            field=models.FloatField(blank=True, default=0, max_length=100, null=True, verbose_name='الوزن'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=100, verbose_name='العنوان'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=100, verbose_name='الايميل'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=100, verbose_name='الاسم'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=100, verbose_name='الهاتف'),
        ),
        migrations.AlterField(
            model_name='out_stock',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='out_stock',
            name='price',
            field=models.FloatField(default=0, max_length=100, verbose_name='السعر'),
        ),
    ]
