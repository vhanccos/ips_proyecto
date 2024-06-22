from django import forms
from .models import Tooth

class ToothForm(forms.ModelForm):
    class Meta:
        model = Tooth
        fields = ['tooth_number', 'is_problematic']