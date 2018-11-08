from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comentario(models.Model):
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post,  on_delete=models.CASCADE)

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text

class Pessoa(User):
    pes_codigo = models.AutoField(primary_key=True)
    pes_nacionalidade = models.CharField(blank=True, null=True, max_length=80, default='Brasileira')
    pes_endereco_completo = models.CharField(max_length=500)
    pes_telefone_p = models.CharField(max_length=20)

    def publish(self):
        self.date_joined = timezone.now()
        self.save()

    def __str__(self):
        return self.first_name
