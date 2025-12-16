# forms.py
from django import forms
from django.core.validators import RegexValidator, EmailValidator

class CheckoutForm(forms.Form):
    first_name = forms.CharField(
        max_length=50,
        validators=[RegexValidator(r'^[a-zA-Z]+$', 'Only letters are allowed')],
        widget=forms.TextInput(attrs={
            'placeholder': 'First Name',
            'class': 'w-full border rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-green-500'
        })
    )
    last_name = forms.CharField(
        max_length=50,
        validators=[RegexValidator(r'^[a-zA-Z]+$', 'Only letters are allowed')],
        widget=forms.TextInput(attrs={
            'placeholder': 'Last Name',
            'class': 'w-full border rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-green-500'
        })
    )
    phone = forms.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\d+$', 'Phone must contain only numbers')],
        widget=forms.TextInput(attrs={
            'placeholder': 'Phone Number',
            'class': 'w-full border rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-green-500'
        })
    )
    email = forms.EmailField(
        validators=[EmailValidator('Enter a valid email')],
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email',
            'class': 'w-full border rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-green-500'
        })
    )
    county = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'placeholder': 'County',
            'class': 'w-full border rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-green-500'
        })
    )
    city = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'placeholder': 'City',
            'class': 'w-full border rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-green-500'
        })
    )
    till_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'placeholder': 'Till Name',
            'class': 'w-full border rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-green-500'
        })
    )
