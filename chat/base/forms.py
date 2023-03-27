from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1','password2')

    username = forms.CharField(widget=forms.TextInput(attrs={

        'placeholder':'Your Username',
        

    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={

        'placeholder':'Your Password',
        

    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={

        'placeholder':'Repeat Password',
        

    }))
