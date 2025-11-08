from django import forms

class ServiceRequestForm(forms.Form):
    full_name = forms.CharField(max_length=150, label="Full name")
    phone_number = forms.CharField(max_length=30, label="Phone number")
    email = forms.EmailField(required=False, label="Email (optional)")
    transaction_code = forms.CharField(max_length=128, required=False, label="Payment transaction code")
