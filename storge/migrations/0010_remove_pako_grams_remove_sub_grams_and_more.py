# Generated by Django 4.1.4 on 2023-02-02 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storge', '0009_alter_pako_grams_alter_pako_linght_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pako',
            name='grams',
        ),
        migrations.RemoveField(
            model_name='sub',
            name='grams',
        ),
        migrations.AlterField(
            model_name='gram_categore',
            name='code',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='gram_categore',
            name='name',
            field=models.FloatField(max_length=5),
        ),
    ]
