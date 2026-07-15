from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control form-control-lg', 
                'placeholder': 'Enter post title...'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 8, 
                'placeholder': 'Write your blog post content here...'
            }),
        }
