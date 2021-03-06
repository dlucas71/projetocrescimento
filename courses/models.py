from django.db import models


class CourseManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) |\
            models.Q(description__icontains=query)
        )

class Course(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho ')
    description = models.TextField('Descrição', blank=True)
    start_date = models.DateField(
        'Data de Inicio', null=True, blank=True
    )
    #--- inserindo uma imagem
    image = models.ImageField(upload_to='courses/imgs', verbose_name='Imagem',
                              null=True, blank=True
    )
    #---Adicionando a data da criacao do curso
    created_at = models.DateTimeField(
        'Criado em', auto_now_add=True
    )
    #---Alterando a data
    updated_at = models.DateTimeField(
        'Atualizado em', auto_now=True
    )

    objects = CourseManager()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        #---Ordenando a lista
        ordering = ['name']
