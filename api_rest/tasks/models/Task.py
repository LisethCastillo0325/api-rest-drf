from django.db import models
from users.models import User

class Task(models.Model):

    name = models.CharField('Nombre', max_length=100)
    description = models.CharField('Descripción', max_length=250);
    user = models.ForeignKey(User, related_name='tasks', on_delete=models.DO_NOTHING, verbose_name='Usuario')
    is_finalized = models.BooleanField('Está Finalizada?', default=False, null=True)
    finish_date = models.DateField('Fecha Finalización', null=True, blank=True)
    create_date = models.DateField('Fecha Creación', auto_now=False, auto_now_add=True)

    def __str__(self):
        return f'{self.id} {self.name} {self.description} {self.is_finalized} {self.finish_date} {self.create_date}'

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'