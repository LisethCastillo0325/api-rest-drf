from django.db import models

class DocumentType(models.Model):

    name = models.CharField('Tipo de Documento', max_length=150);

    def __str__(self):
        return f'{self.id} {self.name}'

    class Meta:
        verbose_name = 'Tipo Documento'
        verbose_name_plural = 'Tipos de Documentos'