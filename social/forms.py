from django import forms
from .models import Post, Comment, UserProfile




class PostForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Drop your views...'
            }))

    image = forms.ImageField(required=False)

    class Meta:
        model = Post
        fields = ['body', 'image']

class PrivateForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Say Something...'
            }))

    image = forms.ImageField(required=False)

    class Meta:
        model = Post
        fields = ['body', 'image']

class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Say Something...'
            }))

    class Meta:
        model = Comment
        fields = ['comment']
