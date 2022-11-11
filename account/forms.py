from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UsercreateFrom(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label='Confirm Password')
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'birth_date', 'gender', 'nationality', 'address', 'image', 'phone_number']
        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'birth_date' : forms.DateInput(attrs={'class':'form-control form-control-lg'}),
            'gender' : forms.Select(attrs={'class':'form-control form-control-lg'}),
            'nationality' : forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'address' : forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'image' : forms.FileInput(attrs={'class':'form-control form-control-lg'}),
            'phone_number' : forms.TextInput(attrs={'class':'form-control form-control-lg'}),
        }