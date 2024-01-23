from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField('Nome', max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Topico(models.Model):
    titulo = models.CharField("Título", max_length=100)
    descricao = models.TextField("Descrição")
    data_criacao = models.DateTimeField(
        "Criado", auto_now=True)
    data_update = models.DateTimeField("Atualizado", auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Usuario")
    tag = models.ManyToManyField(Tag, verbose_name="Tags")
    visualizacao = models.IntegerField("Visualizações", default=0)
    slug = models.SlugField()

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Tópico"
        verbose_name_plural = "Tópicos"


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Usuario")
    post = models.TextField("Post")
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE)
    likes = models.IntegerField("Likes", default=0)

    def __str__(self):

        if len(self.post) > 25:
            return self.post[:25]+" ..."
        else:
            return self.post

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
