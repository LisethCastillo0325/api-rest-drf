from rest_framework import generics
from users.serializers import UserListSerializer
from users.models import User

class UserListAPIView(generics.ListAPIView):
    """
    Listar información detallada de los usuarios.

    Retorna la lista de numeros ordenada, los valores repetidos se mueven al final
    """
    serializer_class = UserListSerializer

    def get_queryset(self):
        return User.objects.all()