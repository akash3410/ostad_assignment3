from django import forms
from .models import Employee

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'address', 'phone', 'short_description']
