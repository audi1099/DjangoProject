from django.db import models
import re
from django.core.exceptions import ValidationError

# Валидаторы
def validate_license_plate(value):
    pattern = r'^\d{4}[A-Z]{2}-\d$'
    if not re.fullmatch(pattern, value):
        raise ValidationError("Госномер должен быть в формате: 1234 AB-7")

def validate_date_format(value):
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    if not re.fullmatch(pattern, str(value)):
        raise ValidationError("Дата должна быть в формате: ГГГГ-ММ-ДД")

# Владелец автомобиля
class Owner(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя владельца")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(unique=True, verbose_name="Email")

    def __str__(self):
        return self.name

# Автомобиль
class Car(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, verbose_name="Владелец", related_name="cars")
    car_make = models.TextField(blank=False, verbose_name="Марка автомобиля", max_length=50)

    license_plate = models.CharField(
        max_length=9,
        unique=True,
        verbose_name="Госномер",
        validators=[validate_license_plate]
    )
    description = models.TextField(blank=True, verbose_name="Описание")

    def __str__(self):
        return f"{self.license_plate} - {self.owner.name}"

# Список возможных услуг
class Service(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название услуги")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    description = models.TextField(blank=True, verbose_name="Описание")  # Добавлено описание

    def __str__(self):
        return self.name

# Ремонт автомобиля
class Repair(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидание'),
        ('in_progress', 'В процессе'),
        ('completed', 'Завершено'),
    ]

    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="Автомобиль", related_name="repairs")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Услуга")
    date = models.DateField(verbose_name="Дата ремонта")
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость ремонта")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Статус")




    def __str__(self):
        return f"{self.service.name} для {self.car.license_plate} ({self.get_status_display()})"

# Запчасти
class Part(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название запчасти")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(verbose_name="Количество на складе")

    def __str__(self):
        return self.name

# Использование запчастей в ремонте
class PartUsage(models.Model):
    repair = models.ForeignKey(Repair, on_delete=models.CASCADE, verbose_name="Ремонт", related_name="part_usages")
    part = models.ForeignKey(Part, on_delete=models.CASCADE, verbose_name="Запчасть", related_name="part_usages")
    quantity = models.PositiveIntegerField(verbose_name="Количество")

    def __str__(self):
        return f"{self.part.name} ({self.quantity} шт.) для {self.repair.car.license_plate}"