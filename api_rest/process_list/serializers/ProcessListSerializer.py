from rest_framework import serializers

class ProcessListSerializer(serializers.Serializer):

    unclassified = serializers.ListField(
        child=serializers.IntegerField(min_value=0, max_value=100)
    )

    def to_representation(self, instance):
        list_data = instance['unclassified']
        return {
            'sin clasificar': list_data,
            'clasificado': self._processList(list_data)
        }

    def _processList(self, list_data):
        repeating_list = []
        initial_list = []
        for i in range(len(list_data)):
            initial_list.append(list_data[i]) if list_data[i] not in initial_list else repeating_list.append(list_data[i])

        initial_list.sort()
        result = initial_list + repeating_list     
        return result




  





