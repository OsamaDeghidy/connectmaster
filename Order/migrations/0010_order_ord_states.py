# Generated by Django 4.0 on 2022-09-12 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0009_order_states'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Ord_states',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Order.order_states', verbose_name='المرحلة'),
        ),
    ]
