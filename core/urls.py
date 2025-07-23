from django.urls import path
from .views import DependencyView

urlpatterns = [
    path('dependencies/<str:cell_id>/', DependencyView.as_view(), name='cell-dependencies'),
]
