from django import forms
from django.forms import ModelForm
from .models import *


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class SignUpForm(ModelForm):
    class Meta:
        model = SignUp
        fields = "__all__"

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    repeated_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data["password"] != cleaned_data["repeated_password"]:
            self.add_error(
                "repeated_password", "repeated password does not equal password."
            )
        return cleaned_data
