from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Branch


class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ("branch_name", "contact_number", "address")
        widgets = {
            "branch_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "e.g. Pune Main Branch"}
            ),
            "contact_number": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "10 digits only", "maxlength": "10"}
            ),
            "address": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Optional street address",
                }
            ),
        }

    def clean_contact_number(self):
        contact_number = self.cleaned_data.get("contact_number", "").strip()
        if not contact_number.isdigit() or len(contact_number) != 10:
            raise forms.ValidationError("Enter a valid 10-digit contact number using digits only.")
        return contact_number


class BranchImportForm(forms.Form):
    file = forms.FileField(
        label="Excel (.xlsx) or CSV file",
        widget=forms.ClearableFileInput(attrs={"class": "form-control", "accept": ".csv,.xlsx"}),
    )


class StaffSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter username",
                    "autocomplete": "username",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter password",
                "autocomplete": "new-password",
            }
        )
        self.fields["password2"].widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Confirm password",
                "autocomplete": "new-password",
            }
        )
