from rest_framework import generics
from users.serializers import UserListSerializer
from users.models import User

class UserListAPIView(generics.ListAPIView):
    
    serializer_class = UserListSerializer

    def get_queryset(self):
        return User.objects.all()