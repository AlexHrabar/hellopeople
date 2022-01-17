from .models import Name
from django.forms import ModelForm, TextInput


class NameForm(ModelForm):
    class Meta:
        model = Name
        fields = ["name"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть ім\'я та прізвище'
            })
        }
