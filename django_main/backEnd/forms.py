from django import forms
from .models import Item


class ItemForm(forms.models.ModelForm):
    class Meta:
        EMPTY_LIST_ERROR = "Element cannot be empty"
        model = Item
        fields = ("text",)
        widgets = {
            "text": forms.fields.TextInput(
                attrs={
                    "placeholder": "Type Thing To Do",
                }
            )
        }
        error_messages = {
            "text": {"required": EMPTY_LIST_ERROR}
        }
