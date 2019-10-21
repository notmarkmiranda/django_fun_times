from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    body = forms.CharField(
        label = 'Comment',
        required = True,
        widget = forms.Textarea(
            attrs = { 'class': 'form-control'}
        )
    )
    class Meta:
        model = Comment
        fields = ('body',)
