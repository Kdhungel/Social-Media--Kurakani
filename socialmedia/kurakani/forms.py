from django import forms
from .models import Kurakani
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class KurakaniForm(forms.ModelForm):
    class Meta:
        model = Kurakani
        fields = ['text', 'photo']
        
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')