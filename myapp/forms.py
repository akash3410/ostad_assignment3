from django import forms
from .models import Employee

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'address', 'phone', 'short_description']

class AddEmployee(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'address', 'phone', 'salary', 'designation', 'short_description']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
            'short_description': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
        }