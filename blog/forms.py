from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "category", "body", "image", "status"]
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'category': forms.Select(attrs={'class':'form-control form-control-lg'}),
            'status': forms.Select(attrs={'class':'form-control form-control-lg'}),
            'body': forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'image': forms.FileInput(attrs={'class':'form-control form-control-lg'}),
        }