from django.contrib.auth.forms import forms
from django.contrib.auth.models import User
from .models import Profile


class UserRegisterForm(forms.ModelForm):
    YEARS = [i for i in range(1935, 2005)]
    username = forms.CharField(max_length=128)
    password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=128)
    last_name = forms.CharField(max_length=128)
    email = forms.EmailField(max_length=250)
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'date_of_birth', ]


class UserUpdateForm(forms.ModelForm):
    YEARS = [i for i in range(1935, 2005)]
    username = forms.CharField(max_length=128)
    password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=128)
    last_name = forms.CharField(max_length=128)
    email = forms.EmailField(max_length=250)
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'date_of_birth', ]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['picture']




