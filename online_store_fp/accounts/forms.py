from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField
    last_name = forms.CharField

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']



