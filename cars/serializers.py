from rest_framework import serializers
from .models import Owner, Car, Service, Repair, Part, PartUsage

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['id', 'name', 'phone', 'email']


class CarSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer()

    class Meta:
        model = Car
        fields = ['id', 'license_plate', 'description', 'owner']

    def create(self, validated_data):
        owner_data = validated_data.pop('owner')
        owner, _ = Owner.objects.get_or_create(**owner_data)
        car = Car.objects.create(owner=owner, **validated_data)
        return car

    def update(self, instance, validated_data):
        owner_data = validated_data.pop('owner', None)
        if owner_data:
            Owner.objects.filter(id=instance.owner.id).update(**owner_data)
        return super().update(instance, validated_data)


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'price']


class RepairSerializer(serializers.ModelSerializer):
    car = CarSerializer()
    service = ServiceSerializer()

    class Meta:
        model = Repair
        fields = ['id', 'car', 'service', 'date', 'cost', 'status']

    def create(self, validated_data):
        car_data = validated_data.pop('car')
        service_data = validated_data.pop('service')

        car, _ = Car.objects.get_or_create(**car_data)
        service, _ = Service.objects.get_or_create(**service_data)

        repair = Repair.objects.create(car=car, service=service, **validated_data)
        return repair


class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = ['id', 'name', 'price', 'stock']


class PartUsageSerializer(serializers.ModelSerializer):
    repair = RepairSerializer()
    part = PartSerializer()

    class Meta:
        model = PartUsage
        fields = ['id', 'repair', 'part', 'quantity']

    def create(self, validated_data):
        repair_data = validated_data.pop('repair')
        part_data = validated_data.pop('part')

        repair, _ = Repair.objects.get_or_create(**repair_data)
        part, _ = Part.objects.get_or_create(**part_data)

        part_usage = PartUsage.objects.create(repair=repair, part=part, **validated_data)
        return part_usage