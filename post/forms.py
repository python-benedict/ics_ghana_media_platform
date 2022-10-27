from django import forms
from .models import Comment, InternationalNewsComment, TechnologicalNewsComment, LocalNewsComment, ArticlesComment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.TimeInput(attrs={'class':'input', 'placeholder':'Enter Comment'}),required=False)
    
    class Meta:
        model = Comment
        fields = ['body', 'user', 'post']
        

class InternationalNewsCommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.TimeInput(attrs={'class':'input', 'placeholder':'Enter Comment'}),required=False)
    
    class Meta:
        model = InternationalNewsComment
        fields = ['body', 'user', 'post']
        
        
class ArticlesCommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.TimeInput(attrs={'class':'input', 'placeholder':'Enter Comment'}),required=False)
    
    class Meta:
        model = ArticlesComment
        fields = ['body', 'user', 'post']
        
  
class TechnologicalNewsCommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.TimeInput(attrs={'class':'input', 'placeholder':'Enter Comment'}),required=False)
    
    class Meta:
        model = TechnologicalNewsComment
        fields = ['body', 'user', 'post'] 
        
class LocalNewsCommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.TimeInput(attrs={'class':'input', 'placeholder':'Enter Comment'}),required=False)
    
    class Meta:
        model = LocalNewsComment
        fields = ['body', 'user', 'post']  
    
    
#registration form
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


#Update profile form
class EditProfileForm(forms.Form):
    username = forms.CharField()
    about_me = forms.CharField(widget=forms.Textarea())
    image = forms.ImageField(required=False)
    
    def __init__(self, original_username, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_username = original_username

    def clean_username(self):
        """
        This function throws an exception if the username has already been 
        taken by another user
        """

        username = self.cleaned_data['username']
        if username != self.original_username:
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError(
                    'A user with that username already exists.')
        return username