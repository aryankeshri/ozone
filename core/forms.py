from django import forms
from django.forms import widgets
from .models import Join
from django.utils.translation import ugettext_lazy as _

class JoinForm(forms.ModelForm):
    class Meta:
        model = Join
        fields = ('name', 'age', 'city', 'contact')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': _('Type your name'), 'class':'form-control', 'id':"p_name"}),
            'age': forms.TextInput(attrs={'placeholder': _('Type your age'), 'class':'form-control', 'id':"p_age"}),
            'city': forms.TextInput(attrs={'placeholder': _('Type your city'), 'class':'form-control', 'id':"p_city"}),
            'contact': forms.TextInput(attrs={'placeholder': _('Type your contact'), 'class':'form-control', 'id':"p_phone"}),
        }
        errors = {
            'name': _('This field is required'),
            'age': _('This field is required'),
            'city': _('This field is required'),
            'contact': _('This field is required'),
        }