from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Owner, Car, Service, Repair, Part, PartUsage
from .serializers import OwnerSerializer, CarSerializer, ServiceSerializer, RepairSerializer, PartSerializer, PartUsageSerializer
from django.shortcuts import render
from .models import Car, Repair


# Функция для отображения списка автомобилей

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/cars.html', {'cars': cars})

def car_details(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    repairs = Repair.objects.filter(car=car).order_by('-date')  # Получаем ремонты для этой машины, сортируя по дате
    return render(request, 'cars/repair_details.html', {'car': car, 'repairs': repairs})

def repair_details(request, repair_id):
    repair = get_object_or_404(Repair, id=repair_id)
    return render(request, 'cars/car_details.html', {'repair': repair})



class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class RepairViewSet(viewsets.ModelViewSet):
    queryset = Repair.objects.all()
    serializer_class = RepairSerializer

class PartViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer

class PartUsageViewSet(viewsets.ModelViewSet):
    queryset = PartUsage.objects.all()
    serializer_class = PartUsageSerializer