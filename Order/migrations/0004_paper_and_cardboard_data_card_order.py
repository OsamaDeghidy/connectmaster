# Generated by Django 4.0 on 2022-09-11 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0003_alter_order_ord_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper_and_cardboard_data',
            name='CARD_Order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Order.order', verbose_name='الامر'),
        ),
    ]
