from django.db.models.deletion import DO_NOTHING
from cities.models.Cities import City
from document_types.models.DocumentType import DocumentType
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from simple_history.models import HistoricalRecords
from users.manager.UserManager import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    
    username      = models.CharField(max_length = 255, unique = True)
    email         = models.EmailField('Correo Electrónico',max_length = 255, unique = True,)
    name          = models.CharField('Nombres', max_length = 255, blank = True, null = True)
    last_name     = models.CharField('Apellidos', max_length = 255, blank = True, null = True)
    document_type = models.ForeignKey(DocumentType, on_delete=models.DO_NOTHING, null=True, verbose_name='Tipo de Documento')
    document      = models.CharField('Documento', max_length=20, null=True)
    city          = models.ForeignKey(City, on_delete=DO_NOTHING, null=True, verbose_name='Ciudad')
    is_active     = models.BooleanField(default = True)
    is_staff      = models.BooleanField(default = False)
    historical    = HistoricalRecords()
    objects       = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','name','last_name']

    def __str__(self):
        return f'{self.id} {self.name} {self.last_name} {self.email} {self.document_type.name} {self.document} {self.city.name}'