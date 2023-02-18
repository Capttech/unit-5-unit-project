from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(max_length=1000, required=True)
