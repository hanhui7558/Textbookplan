from django import forms
from .models import *


class BookOrdForm(forms.ModelForm):
    class Meta:
        model = BookOrd
        fields = '__all__'
