# coding:utf-8
from django import forms

class AddFrom(forms.Form):
    name = forms.CharField()
    content = forms.Textarea()
