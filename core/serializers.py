from rest_framework import serializers
from .models import Cell

class CellDependencySerializer(serializers.Serializer):
    cell_id = serializers.RegexField(
        regex=r'^[A-Z]+[0-9]+$',
        max_length=10,
        required=True
    )
