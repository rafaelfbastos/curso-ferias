from django import forms
from .models import Post, Topico


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["post"]


class TopicoForm(forms.ModelForm):

    class Meta:
        model = Topico
        fields = ['titulo', 'descricao']
