from django.contrib import admin
from .models import Owner, Car, Service, Repair, Part, PartUsage


admin.site.register(Car)
admin.site.register(Owner)
admin.site.register(Service)
admin.site.register(Repair)
admin.site.register(Part)
admin.site.register(PartUsage)