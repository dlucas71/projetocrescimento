from django.db import models

class ArticleManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(title__icontains=query) |
            models.Q(text_article__icontains=query)
        )

class Article(models.Model):
    title = models.CharField('Titulo', max_length=100)
    slug = models.SlugField('Atalho', null=True, blank=True)
    author = models.CharField('Autor', max_length=100)
    reference = models.CharField('Referencia', max_length=100, null=True, blank=True)
    subtitle = models.CharField('Subtitulo', max_length=100)
    text_article = models.TextField('Texto', blank=True)
    start_date = models.DateField(
        'Data da Publicacao', null=True, blank=True
    )
    comentarios = models.TextField('Comentario', blank=True)
    #--- inserindo uma imagem
    image = models.ImageField(upload_to='article/imgs', verbose_name='Imagem',
                              null=True, blank=True
    )
    #---Adicionando a data da criacao do curso
    created_at = models.DateTimeField(
        'Publicado em', auto_now_add=True
    )
    #---Alterando a data
    updated_at = models.DateTimeField(
        'Atualizado em', auto_now=True
    )

    objects = ArticleManager()
    #---Exibindo o titulo do artigo
    def __str__(self):
        return self.title
    #---traduzindo o nome da classe
    class Meta:
        verbose_name = 'Artigo'
        verbose_name_plural = 'Artigos'
        #---Ordenando a lista
        ordering = ['title']
