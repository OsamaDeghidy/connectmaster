# Generated by Django 4.1.4 on 2023-02-02 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storge', '0007_alter_iteam_code_alter_iteam_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='in_stock',
            name='pako',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='storge.pako'),
        ),
        migrations.AddField(
            model_name='in_stock',
            name='pukker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='storge.pukker'),
        ),
        migrations.AddField(
            model_name='in_stock',
            name='sub',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='storge.sub'),
        ),
    ]
