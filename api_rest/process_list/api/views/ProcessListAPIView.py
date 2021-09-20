from process_list.serializers.ProcessListSerializer import ProcessListSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class ProcessListAPIView(APIView):
    """
    Procesar una matriz de números. 
    """
    def post(self, request):
        data = request.data
        try:
            data_serializer = ProcessListSerializer(data = {'unclassified': data['sin clasificar']})
            result = data_serializer.data if  data_serializer.is_valid() else data_serializer.errors
            return Response(result, status = status.HTTP_200_OK)
        except KeyError as e:
            return Response({'error': f'Error de llave {e}'}, status = status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': f'{e}'}, status = status.HTTP_400_BAD_REQUEST)
                 