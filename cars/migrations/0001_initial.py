# Generated by Django 5.1.6 on 2025-02-13 20:37

import cars.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя владельца')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название запчасти')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('stock', models.PositiveIntegerField(verbose_name='Количество на складе')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название услуги')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate', models.CharField(max_length=9, unique=True, validators=[
                    cars.models.validate_license_plate], verbose_name='Госномер')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='cars.owner', verbose_name='Владелец')),
            ],
        ),
        migrations.CreateModel(
            name='Repair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата ремонта')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стоимость ремонта')),
                ('status', models.CharField(choices=[('pending', 'Ожидание'), ('in_progress', 'В процессе'), ('completed', 'Завершено')], default='pending', max_length=20, verbose_name='Статус')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='repairs', to='cars.car', verbose_name='Автомобиль')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.service', verbose_name='Услуга')),
            ],
        ),
        migrations.CreateModel(
            name='PartUsage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество')),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='part_usages', to='cars.part', verbose_name='Запчасть')),
                ('repair', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='part_usages', to='cars.repair', verbose_name='Ремонт')),
            ],
        ),
    ]
