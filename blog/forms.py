from django import forms
from .models import Post, Comment

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

class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget = forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = Comment
        fields = ["comment"]