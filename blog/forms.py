from django import forms
from blog.models import Post, Comments

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'text', 'tags')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text' : forms.Textarea(attrs={'class': 'editable medium-editor-textarea posttext'}),

            'tags': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('text',)

        widgets = {
            'text' : forms.Textarea(attrs={'class':'comment-textarea'})
        }

        labels = {
            'text': ''
        }