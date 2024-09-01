from ast import Attribute, FormattedValue
from cProfile import label
from email.policy import default
from random import choices
import arabic_reshaper as _
from pyexpat import model
from tkinter import Widget
from django import forms

from Order.models import Order
from .models import Machine, Machine_Order


class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['machine_name', 'machine_code']
        
        
        
class Machine_OrderForm(forms.ModelForm):
    machine = forms.ModelMultipleChoiceField(
        queryset=Machine.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={'style': 'margin-bottom: 13px;'}
        ),
    )

    order = forms.ModelChoiceField(
        queryset=Order.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    paper_processing = forms.IntegerField(label='تجهيز ورق', required=False,widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'تجهيز ورق'}),)
    gto1_print_quarter = forms.IntegerField(label='GTO(1) طباعة ربع', required=False,widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'GTO(1) طباعة ربع'}),)
    sm2_print_quarter = forms.IntegerField(label='SM(2) طباعة ربع', required=False,widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'SM(2) طباعة ربع'}),)
    sm5_print_quarter = forms.IntegerField(label='SM(5) طباعة ربع', required=False,widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'SM(5) طباعة ربع'}),)
    sorm_print_half = forms.IntegerField(label='SORM طباعة نص', required=False,widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'SORM طباعة نص'}),)
    sm2_print_half = forms.IntegerField(label='SM(2) طباعة نص', required=False,widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'SM(2) طباعة نص'}),)
    sm_print_chick = forms.IntegerField(label='SM طباعة فرخ', required=False,widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'SM طباعة فرخ'}),)
    cd5_print_chick = forms.IntegerField(label='CD(5) طباعة فرخ', required=False,widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'CD(5) طباعة فرخ'}),)
    lamination = forms.IntegerField(label='سلوفان', required=False,widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'سلوفان'}),)
    printing_varnish_services_uv = forms.IntegerField(label='خدمات طباعة ورنيش/يوفي', required=False,widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'خدمات طباعة ورنيش/يوفي'}),)
    external_printing_services = forms.IntegerField(label='خدمات طباعة خارجي', required=False,widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'خدمات طباعة خارجي'}),)
    die_cutting_46 = forms.IntegerField(label='DIE 46 تكسير', required=False,widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'DIE 46 تكسير'}),)
    die_cutting_57 = forms.IntegerField(label='DIE 57 تكسير', required=False,widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'DIE 57 تكسير'}),)
    bobst_die_cutting = forms.IntegerField(label='BOBST تكسير', required=False,widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'BOBST تكسير'}),)
    wiring_and_cleaning = forms.IntegerField(label='التسليك و التنظيف', required=False,widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'التسليك و التنظيف'}),)
    pactek_85_gluing = forms.IntegerField(label='PACTEK 85 تلزيق', required=False,widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'PACTEK 85 تلزيق'}),)
    pactek_65_gluing = forms.IntegerField(label='PACTEK 65 تلزيق', required=False,widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'PACTEK 65 تلزيق'}),)
    fg_gluing = forms.IntegerField(label='FG تلزيق', required=False,widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'FG تلزيق'}),)
    sbl_gluing = forms.IntegerField(label='SBL تلزيق', required=False,widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'SBL تلزيق'}),)
    manual_gluing = forms.IntegerField(label='تلزيق يدوي', required=False,widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'تلزيق يدوي'}),)
    binding = forms.IntegerField(label='تجليد', required=False,widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'تجليد'}),)
    finished_goods_cutting = forms.IntegerField(label='قص بضاعة منتهية', required=False,widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'قص بضاعة منتهية'}),)
    external_gluing = forms.IntegerField(label='تلزيق خارجي', required=False,widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'تلزيق خارجي'}),)

    class Meta:
        model = Machine_Order
        fields = '__all__'
            

