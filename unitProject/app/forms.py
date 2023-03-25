from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# ========|bryan's work==============#
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ["user", "date_created", "uid", "profile_pic"]
        widgets = {
            "profile_pic": forms.FileInput(),
        }


class BusinessForm(forms.ModelForm):
    creationDate = models.DateField(auto_now_add=True)

    class Meta:
        model = businessTemplateDatabase
        fields = ["name", "description", "type", "missionStatement"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
            "missionStatement": forms.Textarea(attrs={"rows": 8}),
        }


class BusinessContactInfoForm(forms.ModelForm):
    class Meta:
        model = businessContactInfoDatabase
        fields = ["email", "phone_number", "address"]


class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ["user", "template"]

    #     business_contact_info = BusinessContactInfoForm()

    def __init__(self, *args, **kwargs):
        super(SubmissionForm, self).__init__(*args, **kwargs)
        self.fields["user"].queryset = Profile.objects.filter(user=self.instance.user)


# =============| end of bryan's work |===============#
