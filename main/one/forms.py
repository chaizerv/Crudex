from django import forms
from .models import Crudex


class CrudexForm(forms.ModelForm):
    class Meta:
        model = Crudex
        fields = ('username','first_name','last_name','password', 'is_active')
        labels = {'first_name':'First name',
                  'last_name':'Last name',
                  'is_active':'Active'
        }
