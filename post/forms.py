from django import forms
from .models import Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.TimeInput(attrs={'class':'input', 'placeholder':'Enter Comment'}),required=False)
    
    class Meta:
        model = Comment
        fields = ['body', 'user', 'post']
    
    
#registration form
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
