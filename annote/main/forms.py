from . models import Annote
from django.forms import ModelForm, Textarea, TextInput


class WriteForm(ModelForm):
    class Meta:
        model = Annote
        fields = ['annote']

        widgets = {
            "annote": Textarea(attrs={
                'class': 'write-form form-center',
                'placeholder': 'Enter your anNote',
            })
        }


class ReadForm(ModelForm):
    class Meta:
        model = Annote
        fields = ['link']

        widgets = {
            "link": TextInput(attrs={
                'class': 'read-form form-center',
                'placeholder': 'Enter the password',
            })
        }

