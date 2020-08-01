from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Resume

class UserRegistrationForm (UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    
class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['resume',]