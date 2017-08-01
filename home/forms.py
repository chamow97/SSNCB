from django.contrib.auth.models import User
from django import forms
from django.forms import EmailField


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        widgets = {
            'username': forms.TextInput(),
            'email': forms.EmailInput(),
            'password': forms.PasswordInput(),
        }
        fields = ['username', 'email', 'password']

