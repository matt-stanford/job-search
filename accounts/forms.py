from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm (UserCreationForm):
    email = forms.EmailField()
    resume = forms.FileField(upload_to='documents/', blank=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'resume', 'password1', 'password2']