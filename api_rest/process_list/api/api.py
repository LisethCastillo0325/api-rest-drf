from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

import json

class ProcessListAPIView(APIView):

    def post(self, request):
        
        try:
            data = json.loads(request.body)
            list_data = list(data['sin clasificar'])
            data = {
                'sin clasificar': list_data,
                'clasificado':  self._processList(list_data)
            }
            return Response(data, status = status.HTTP_200_OK)
        except KeyError as e:
            return Response({'error': f'Error de llave {e}'}, status = status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': f'{e}'}, status = status.HTTP_400_BAD_REQUEST)
        


    def _getRepeactValues(self, list_data):
        ordered_list = sorted(list_data)
        repeating_list = []
        for i in range(len(ordered_list)):
            item = ordered_list[i]
            previous_item = ordered_list[i-1]
            if item == previous_item:
                repeating_list.append(item)
        return repeating_list


    def _processList(self, list_data):
        repeact_values = self._getRepeactValues(list_data);
        result = list(set(list_data))
        return result + repeact_values


       