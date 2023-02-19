from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _
from .models import Customer


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label = "Enter Password", widget=forms.PasswordInput(attrs={'class':"form-control"}))
    password2 = forms.CharField(label = "Confirm Password",  widget=forms.PasswordInput(attrs={'class':"form-control"}))
    email = forms.CharField(label="Email",required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
        }

class LoginForm(AuthenticationForm):    
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True, 'class':'form-control'}))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", 'class':'form-control'}),
    )


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "autofocus": True, 'class':'form-control'}
        ),
    )
    new_password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class':'form-control'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )



class CustomerForm(forms.ModelForm): 
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-control'}))    
    locality = forms.CharField(label='Locality', widget=forms.TextInput(attrs={'class': 'form-control'}))    
    city = forms.CharField(label='City', widget=forms.TextInput(attrs={'class': 'form-control'}))    
    zipcode = forms.CharField(label='Zipcode', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # state = forms.CharField(label='State', widget=forms.TextInput(attrs={'class': 'form-control'}))
    

    class Meta:
        model = Customer
        fields = ['name', 'locality', 'city', 'zipcode', 'state']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'zipcode': forms.NumberInput(attrs={'class': 'form-control'}),
            
            'state': forms.Select(attrs={'class':'form-control'}),
        }
    
