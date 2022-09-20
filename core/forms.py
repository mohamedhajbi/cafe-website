from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from . import models  

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


    

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        User = models.User
        fields=('content',)
        
