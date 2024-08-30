from django import forms
from .models import Kurakani

class KurakaniForm(forms.ModelForm):
    class Meta:
        model = Kurakani
        fields = ['text', 'photo']
        