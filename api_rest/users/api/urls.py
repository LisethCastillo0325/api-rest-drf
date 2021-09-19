from django.urls import path
from users.api.views.UserListAPIView import UserListAPIView

urlpatterns = [
    path('', UserListAPIView.as_view(), name='usuario')
]

