from django import forms

from .models import Post

class Post_Create_Forms(forms.ModelForm):
    class Meta: ## La clase Meta se utiliza para proporcionar metadatos adicionales al formulario, como el modelo base y los campos que se deben incluir.
        model=Post
        fields=('title', 'content')