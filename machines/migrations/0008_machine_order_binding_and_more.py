# Generated by Django 4.2.9 on 2024-06-30 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0007_remove_machine_order_machines_machine_order_machine_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine_order',
            name='binding',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='تجليد'),
        ),
        migrations.AddField(
            model_name='machine_order',
            name='bobst_die_cutting',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='BOBST تكسير'),
        ),
        migrations.AddField(
            model_name='machine_order',
            name='cd5_print_chick',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='CD(5) طباعة فرخ'),
        ),
        migrations.AddField(
            model_name='machine_order',
            name='die_cutting_46',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='DIE 46 تكسير'),
        ),
        migrations.AddField(
            model_name='machine_order',
            name='die_cutting_57',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='DIE 57 تكسير'),
        ),
        migrations.AddField(
            model_name='machine_order',
            name='external_gluing',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='تلزيق خارجي'),
        ),
        migrations.AddField(
            model_name='machine_order',
            name='external_printing_services',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='خدمات طباعة خارجي'),
        ),
        migrations.AddField(
            model_name='machine_order',
            name='fg_gluing',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='FG  تلزيق'),
        ),
        migrations.AddField(
            model_name='machine_order',
            name='finished_goods_cutting',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='قص بضاعة منتهية'),
        ),
        migrations.AddField(
            model_name='machine_order',
            name='gto1_print_quarter',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='GTO(1) طباعة ربع'),
        ),
        migrations.AddField(
            model_name='machine_order',
            name='lamination',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='سلوفان'),
        ),
        migrations.AddField(
            model_name='machine_order',
            name='manual_gluing',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='تلزيق يدوي'),
        ),
        migrations.AddField(
            model_name='machine_order',
            name='pactek_65_gluing',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='PACTEK 65 تلزيق'),
        ),
        migrations.AddField(
            model_name='machine_order',
            name='pactek_85_gluing',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='PACTEK 85 تلزيق'),
        ),
        migrations.AddField(
            model_name='machine_order',
            name='paper_processing',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='تجهيز ورق'),
        ),
        migrations.AddField(
            model_name='machine_order',
            name='printing_varnish_services_uv',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='خدمات طباعة ورنيش/يوفي'),
        ),
        migrations.AddField(
            model_name='machine_order',
            name='sbl_gluing',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='SBL  تلزيق'),
        ),
        migrations.AddField(
            model_name='machine_order',
            name='sm2_print_half',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='SM(2) طباعة نص'),
        ),
        migrations.AddField(
            model_name='machine_order',
            name='sm2_print_quarter',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='SM(2) طباعة ربع'),
        ),
        migrations.AddField(
            model_name='machine_order',
            name='sm5_print_quarter',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='SM(5) طباعة ربع'),
        ),
        migrations.AddField(
            model_name='machine_order',
            name='sm_print_chick',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='SM طباعة فرخ'),
        ),
        migrations.AddField(
            model_name='machine_order',
            name='sorm_print_half',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='SORM طباعة نص'),
        ),
        migrations.AddField(
            model_name='machine_order',
            name='wiring_and_cleaning',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='التسليك و التنظيف'),
        ),
    ]
