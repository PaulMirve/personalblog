from django import forms
from blog.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'text', 'tags')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text' : forms.Textarea(attrs={'class': 'editable medium-editor-textarea posttext'}),

            'tags': forms.TextInput(attrs={'class': 'form-control'}),
        }