from django.db import models

class City(models.Model):

    name = models.CharField('Ciudad', max_length=250, null=False)

    def __str__(self):
        # return f'{self.id} {self.name}'
        return '%d: %s' % (self.id, self.name)

    
    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'