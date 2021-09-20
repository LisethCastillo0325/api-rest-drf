from rest_framework import generics
from users.serializers import UserListSerializer
from users.models import User

class UserListAPIView(generics.ListAPIView):
    """
    Listar información detallada de los usuarios.

    Se lista información del usuario, su tipo de documento, ciudad y tareas asociadas
    """
    serializer_class = UserListSerializer

    def get_queryset(self):
        return User.objects.all()