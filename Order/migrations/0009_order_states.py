# Generated by Django 4.0 on 2022-09-12 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0008_alter_order_ord_code_edited_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_states',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='الاسم')),
            ],
        ),
    ]
