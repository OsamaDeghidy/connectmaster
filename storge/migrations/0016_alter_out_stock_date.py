# Generated by Django 4.1.4 on 2023-02-06 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storge', '0015_alter_pako_iteam_alter_pukker_iteam_alter_sub_iteam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='out_stock',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
