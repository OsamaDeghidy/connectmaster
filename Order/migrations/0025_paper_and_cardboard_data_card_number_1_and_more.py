# Generated by Django 4.0 on 2022-09-24 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0024_paper_and_cardboard_data_card_gross_weight_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper_and_cardboard_data',
            name='CARD_Number_1',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='العدد'),
        ),
        migrations.AddField(
            model_name='paper_and_cardboard_data',
            name='CARD_Number_2',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='العدد'),
        ),
    ]
