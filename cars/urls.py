from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OwnerViewSet, CarViewSet, ServiceViewSet, RepairViewSet, PartViewSet, PartUsageViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from . import views
router = DefaultRouter()
router.register(r'owners', OwnerViewSet)
router.register(r'cars', CarViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'repairs', RepairViewSet)
router.register(r'parts', PartViewSet)
router.register(r'part-usages', PartUsageViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('cars/<int:car_id>/', views.car_details, name='car_details'),
    path('repair/<int:repair_id>/', views.repair_details, name='repair_details'),
    path('car/<int:car_id>/details/', views.car_details, name='car_details'),
    path('cars/', views.car_list, name='car_list'),  # Новый маршрут для списка автомобилей
    path('car/<int:car_id>/details/', views.car_details, name='car_details'),
    path('repair/<int:repair_id>/details/', views.repair_details, name='repair_details'),

]