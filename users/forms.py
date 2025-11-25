'''
This file contains all form classes created in users app.
'''
from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# This is the form for the creation of new users.
class CustomUserModelForm(forms.ModelForm):
    password1 = forms.CharField(required=False)
    password2 = forms.CharField(required=False)
    class Meta:
        model = CustomUser # This connects the form to the custom user model.
        fields = ['first_name', 'last_name', 'other_names', 'profile_picture', 'gender',
                           'date_of_birth', 'role', 'address', 'emergency_contact'] # These are the fields filled to create a new user.


# This is the form used to edit the info of already existing users.
class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser # This connects the form to the custom user model.
        fields = ['first_name', 'last_name', 'other_names', 'profile_picture', 'gender',
                           'date_of_birth', 'role', 'address', 'emergency_contact'] # These are the fields used to edit users information.