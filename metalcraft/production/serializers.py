from rest_framework import serializers
from .models import RawMaterial, Product, WorkOrder, WorkStation, ProductionStage, ProductRawMaterial, ProductWorkStation

class RawMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawMaterial
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class WorkOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = '__all__'

class WorkStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkStation
        fields = '__all__'

class ProductionStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionStage
        fields = '__all__'

class ProductRawMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRawMaterial
        fields = '__all__'

class ProductWorkStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductWorkStation
        fields = '__all__'
