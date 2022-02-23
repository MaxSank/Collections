from django import forms
from django.db import models
from django.forms import ModelForm, TextInput, Textarea, EmailInput
from .models import ItemCollection


class ItemCollectionCreationForm(ModelForm):
    """name = forms.CharField(max_length=150)
    description = forms.CharField(
        widgets=forms.Textarea(attrs={'class': 'form-control'})
    )
    theme = forms.ChoiceField()"""

    class Meta:
        model = ItemCollection
        fields = ('name', 'description', 'theme')
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'theme': forms.Select(attrs={'class': 'form-control'}),
        }
