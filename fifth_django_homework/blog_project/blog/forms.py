from django import forms
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'maxlength': 500, 'rows': 4}),
        }

    def clean_text(self):
        text = self.cleaned_data.get('text', '')

        if len(text) > 500:
            raise ValidationError("Comment cannot be longer than 500 characters.")

        stripped_text = strip_tags(text)
        if stripped_text != text:
            raise ValidationError("HTML tags are not allowed in comments.")

        return text