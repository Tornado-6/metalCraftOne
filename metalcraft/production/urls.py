from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'raw-materials', views.RawMaterialViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'work-orders', views.WorkOrderViewSet)
router.register(r'workstations', views.WorkStationViewSet)
router.register(r'production-stages', views.ProductionStageViewSet)
router.register(r'product-raw-materials', views.ProductRawMaterialViewSet)
router.register(r'product-workstations', views.ProductWorkStationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
