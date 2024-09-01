# Generated by Django 4.2.9 on 2024-01-28 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0036_alter_order_states_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_states',
            name='name',
            field=models.CharField(choices=[('جديد', 'جديد'), ('تصميم', 'تصميم'), ('مونتاج', 'مونتاج'), ('سلوفان', 'سلوفان'), ('شراء ورق', 'شراء ورق'), ('ورق', 'ورق'), ('شيتر', 'شيتر'), ('تجهيز ورق', 'تجهيز ورق'), ('GTO(1) طباعة ربع', 'GTO(1) طباعة ربع'), ('SM(2) طباعة ربع', 'SM(2) طباعة ربع'), ('SM(5) طباعة ربع', 'SM(5) طباعة ربع'), ('SORM طباعة نص', 'SORM طباعة نص'), ('SM(2) طباعة نص', 'SM(2) طباعة نص'), ('SM طباعة فرخ', 'SM طباعة فرخ'), ('CD(5) طباعة فرخ', 'CD(5) طباعة فرخ'), ('سلوفان', 'سلوفان'), ('خدمات طباعة ورنيش/يوفي', 'خدمات طباعة ورنيش/يوفي'), ('خدمات طباعة خارجي', 'خدمات طباعة خارجي'), ('DIE 46 تكسير', 'DIE 46 تكسير'), ('DIE 57 تكسير', 'DIE 57 تكسير'), ('BOBST تكسير', 'BOBST تكسير'), ('التسليك و التنظيف', 'التسليك و التنظيف'), ('PACTEK 85 تلزيق', 'PACTEK 85 تلزيق'), ('PACTEK 65 تلزيق', 'PACTEK 65 تلزيق'), ('FG  تلزيق', 'FG  تلزيق'), ('SBL  تلزيق', 'SBL  تلزيق'), ('تلزيق يدوي', 'تلزيق يدوي'), ('تجليد', 'تجليد'), ('قص بضاعة منتهية', 'قص بضاعة منتهية'), ('تلزيق خارجي', 'تلزيق خارجي'), ('Closed', 'Closed'), ('حسابات', 'حسابات'), ('Invoiced', 'Invoiced'), ('Deleted', 'Deleted')], default='جديد', max_length=50, verbose_name='الاسم'),
        ),
    ]
