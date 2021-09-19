from django.urls import path
from process_list.api.api import ProcessListAPIView

urlpatterns = [
    path('', ProcessListAPIView.as_view(), name='procesar-lista')
]
