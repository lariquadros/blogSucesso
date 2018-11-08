from django.contrib import admin
from .models import Post
from .models import Comentario
from .models import Pessoa

admin.site.register(Post)
admin.site.register(Comentario)
admin.site.register(Pessoa)