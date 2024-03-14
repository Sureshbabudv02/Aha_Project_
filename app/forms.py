from django import forms
from app.models import *
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        help_texts={'username':''}
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'})
            }
        labels={
            'username':'',
            'password':'',
            'email':''
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['address','profile_pic']
        widgets = {
            'address':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Address'}),
            # 'profile_pic':forms.ImageField()
        }
        labels = {
            'address':'',
            'profile_pic':''
        }