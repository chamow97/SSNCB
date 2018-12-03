from django.contrib.auth.models import User
from django import forms
from django.forms import EmailField


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control reg-field inlineBlock'}))

    class Meta:
        model = User
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username', 'class':'form-control reg-field inlineBlock'}),
            'email': forms.EmailInput(attrs={'placeholder': 'E-mail', 'class':'form-control reg-field inlineBlock'}),
            'password': forms.PasswordInput(),
        }
        fields = ['username', 'email', 'password']


