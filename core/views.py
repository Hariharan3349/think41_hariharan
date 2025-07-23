from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Cell, CellDependency
from .serializers import CellDependencySerializer

class DependencyView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, cell_id):
        serializer = CellDependencySerializer(data={"cell_id": cell_id})
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            cell = Cell.objects.get(cell_id=cell_id)
        except Cell.DoesNotExist:
            return Response({'error': 'Cell not found'}, status=status.HTTP_404_NOT_FOUND)

        dependents = CellDependency.objects.filter(depends_on=cell).select_related('cell')
        data = [d.cell.cell_id for d in dependents]

        return Response({'cell': cell_id, 'dependents': data}, status=status.HTTP_200_OK)
