from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from .models import *

class Loginform(forms.Form):
    username=forms.CharField( widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField( widget=forms.PasswordInput(attrs={'class':'form-control'}))

class Registerform(UserCreationForm):
    username=forms.CharField( widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields=("username","email","password1","password2")
    
class Passchangeform(PasswordChangeForm):
    old_password=forms.CharField(label='Old password ', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1=forms.CharField(label='New password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2=forms.CharField(label='Confirm new password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

        
class Profileform(forms.ModelForm):
    class Meta:
        model = Profile
        exclude =('user',)
# class Registerform(forms.ModelForm):
#     password1=forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
#     class Meta:
#         model = User
#         fields = ('username','email','password','password1')


# class Registerform(forms.ModelForm):
#     password1=forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
#     class Meta:
#         model = User
#         fields = ('username','email','password','password1')