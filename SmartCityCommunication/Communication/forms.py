from django import forms
from .models import *

class SenderForm(forms.ModelForm):
    class Meta:
        model = Sender
        fields = ['von','grund','nachricht']
        widgets = {
            'von': forms.EmailInput(attrs={'class': 'email-control'}),
            'grund': forms.TextInput(attrs={'class': 'betreff-control'}),
            'nachricht': forms.Textarea(attrs={'class': 'nachricht-control', 'cols': '30'})
        }

