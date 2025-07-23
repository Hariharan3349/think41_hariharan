from django.db import models

class Cell(models.Model):
    cell_id = models.CharField(max_length=10, unique=True)

class CellDependency(models.Model):
    cell = models.ForeignKey(Cell, related_name='dependents', on_delete=models.CASCADE)
    depends_on = models.ForeignKey(Cell, related_name='dependencies', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('cell', 'depends_on')
