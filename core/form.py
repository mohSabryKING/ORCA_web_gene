from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Add_user(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1','password2')




class Country_form(forms.ModelForm):
    class Meta:
        model = Client_country
        fields = "__all__"




class Client_ask(forms.ModelForm):
    class Meta:
        model = Client_requests
        fields = '__all__'