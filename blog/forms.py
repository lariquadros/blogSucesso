from django import forms
from .models import Post
from .models import Comentario
from .models import Pessoa

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ('text', )

class PessoaForm(forms.ModelForm):

    class Meta:
        model = Pessoa
        fields = ('username', 'password', 'first_name', 'last_name', 'email', 'pes_nacionalidade', 'pes_endereco_completo', 'pes_telefone_p', )