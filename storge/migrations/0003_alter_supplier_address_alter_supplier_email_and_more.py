# Generated by Django 4.1.4 on 2023-01-26 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storge', '0002_supplier_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='address',
            field=models.CharField(max_length=100, verbose_name='العنوان'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='email',
            field=models.EmailField(max_length=100, verbose_name='الايميل'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='name',
            field=models.CharField(max_length=100, verbose_name='الاسم'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='phone',
            field=models.CharField(max_length=100, verbose_name='الهاتف'),
        ),
    ]
