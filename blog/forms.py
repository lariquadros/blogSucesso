from django import forms
from .models import Post
from .models import Comentario

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ('text', )