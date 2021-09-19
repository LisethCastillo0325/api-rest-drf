from tasks.serializers.TaskSerializer import TaskSerializer
from rest_framework import serializers
from users.models import User

class UserListSerializer(serializers.ModelSerializer):

    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'id', 
            'username', 
            'email', 
            'name', 
            'last_name', 
            'document', 
            'is_active', 
            'document_type', 
            'city',
            'tasks'
        ]
        depth = 2   

    # def to_representation(self,instance):
    #     return {
    #         'id': instance['id'],
    #         'username': instance['username'],
    #         'email': instance['email'],
    #         'password': instance['password'],
    #         'city': instance['city']
    #     }