from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserAddForm(UserCreationForm):
    phoneno = forms.CharField(max_length=10,help_text='Enter 10 digit number')
    #order of form

    class Meta:
        model = User
        fields = ['username','phoneno','password1','password2']