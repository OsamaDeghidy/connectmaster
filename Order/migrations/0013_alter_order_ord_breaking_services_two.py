# Generated by Django 4.0 on 2022-09-19 12:14

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0012_order_ord_breaking_services_two_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Ord_Breaking_services_two',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('شباك جديد', 'شباك جديد'), ('شباك قديم', 'شباك قديم')], default=0, max_length=100, null=True, verbose_name='خدمات التكسير'),
        ),
    ]
