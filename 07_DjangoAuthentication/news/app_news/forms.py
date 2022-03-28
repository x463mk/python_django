from django.forms import Textarea, TextInput

from .models import News, Comment
from django import forms


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'


class CommentFormIsAuth(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user_comment',)
        widgets = {'user_comment': Textarea(attrs={'cols': 35, 'rows': 5})}


class CommentFormNotIsAuth(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user_name', 'user_comment')
        widgets = {
            'user_name': TextInput,
            'user_comment': Textarea(attrs={'cols': 30, 'rows': 5})
            }
