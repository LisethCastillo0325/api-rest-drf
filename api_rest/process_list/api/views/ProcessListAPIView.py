from django.http.response import JsonResponse
from process_list.serializers.ProcessListSerializer import ProcessListSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class ProcessListAPIView(APIView):
    """
    Procesar una matriz de números. 

    Retorna la lista de numeros ordenada, los valores repetidos se mueven al final
    """
    def post(self, request):
        data = request.data
        try:
            data_serializer = ProcessListSerializer(data = {'unclassified': data['sin clasificar']})
            if not data_serializer.is_valid():
                raise Exception(data_serializer.errors)

            return Response(data_serializer.data, status = status.HTTP_200_OK)
        except KeyError as e:
            return Response({'error': f'Error de llave {e}'}, status = status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': f'{e}'}, status = status.HTTP_400_BAD_REQUEST)
                 