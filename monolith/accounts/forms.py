from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
