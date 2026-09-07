from django import forms
from .models import Invitee


class InviteeForm(forms.ModelForm):
    class Meta:
        model = Invitee
        fields = [
            "name",
            "side",
            "relationship",
            "guest_count",
            "events_invited",
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "e.g., Uncle John & Family or Divya Mathew",
                    "required": True,
                }
            ),
            "side": forms.Select(
                attrs={
                    "class": "form-select",
                    "required": True,
                }
            ),
            "relationship": forms.Select(
                attrs={
                    "class": "form-select",
                    "required": True,
                }
            ),
            "guest_count": forms.NumberInput(
                attrs={
                    "class": "form-input",
                    "min": "1",
                    "value": "1",
                    "required": True,
                }
            ),
            "events_invited": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
        }
