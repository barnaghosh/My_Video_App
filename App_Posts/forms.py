from django import forms
from django.forms import fields
from App_Posts.models import Post,Likes,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['video','website','caption','catagory','description',]

class WebForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['website','caption','catagory','description',]




class CommentForm(forms.ModelForm):
    comment = forms.CharField(required=True,label='', widget=forms.Textarea(attrs={'rows': 1, 'cols': 70,'placeholder':'Enter your comment'}))
    class Meta:
        model=Comment
        fields=('comment',)