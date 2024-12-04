from rest_framework import viewsets
from .models import RawMaterial, Product, WorkOrder, WorkStation, ProductionStage, ProductRawMaterial, ProductWorkStation
from .serializers import RawMaterialSerializer, ProductSerializer, WorkOrderSerializer, WorkStationSerializer, ProductionStageSerializer, ProductRawMaterialSerializer, ProductWorkStationSerializer

class RawMaterialViewSet(viewsets.ModelViewSet):
    queryset = RawMaterial.objects.all()
    serializer_class = RawMaterialSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class WorkOrderViewSet(viewsets.ModelViewSet):
    queryset = WorkOrder.objects.all()
    serializer_class = WorkOrderSerializer

class WorkStationViewSet(viewsets.ModelViewSet):
    queryset = WorkStation.objects.all()
    serializer_class = WorkStationSerializer

class ProductionStageViewSet(viewsets.ModelViewSet):
    queryset = ProductionStage.objects.all()
    serializer_class = ProductionStageSerializer

class ProductRawMaterialViewSet(viewsets.ModelViewSet):
    queryset = ProductRawMaterial.objects.all()
    serializer_class = ProductRawMaterialSerializer

class ProductWorkStationViewSet(viewsets.ModelViewSet):
    queryset = ProductWorkStation.objects.all()
    serializer_class = ProductWorkStationSerializer
