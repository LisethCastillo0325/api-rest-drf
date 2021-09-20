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

    def _getRepeactValues(self, list_data):
        ordered_list = sorted(list_data)
        repeating_list = []
        for i in range(len(ordered_list)):
            item = ordered_list[i]
            previous_item = ordered_list[i-1]
            repeating_list.append(item) if item == previous_item else None
                
        return repeating_list


    def _processList(self, list_data):
        repeact_values = self._getRepeactValues(list_data);
        result = list(set(list_data))
        return result + repeact_values


  





