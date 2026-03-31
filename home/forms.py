from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll', 'branch', 'email', 'image']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'roll': forms.NumberInput(attrs={'class': 'form-control'}),
            'branch': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
