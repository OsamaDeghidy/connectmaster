# Generated by Django 4.2.9 on 2024-01-28 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0039_alter_order_ord_states'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Ord_states',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Order.order_states', verbose_name='المرحلة'),
        ),
    ]
