from django import forms

from .models import Post

class Post_Create_Forms(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title', 'content')