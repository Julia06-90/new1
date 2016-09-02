from django import forms
rom django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User, UserManager

class FeedbackForm(forms.Form):
    new_comment = forms.CharField(
        label='Super-duper comment',
        help_text='Ashow? WRITE COMMENT',
        widget=forms.TextInput(attrs={'name':'new_comment','cols':30, 'rows':10, 'placeholder': 'Type your text'})
    )



class Registration(models.Model):
    login = forms.CharField(
        label = "login",
        help_text = "login",
        max_length = 100
    )
    name = forms.CharField(
        label = "your name",
        help_text = "write your name",
        max_length = 20
    )
    surname = forms.CharField(
        label = "your surname",
        help_text = "write your surname",
        max_length = 50
    )
    password = forms.CharField(
        label = "enter password",
        help_text = "enter password",
        max_length = 100
    )
    sender = forms.EmailField()

    class RegistrationForm(ModelForm):
        class Meta:
            model = User
            fields = ['login', 'name', 'surname', 'password', 'sender']























