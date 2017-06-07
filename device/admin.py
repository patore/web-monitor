from django.contrib import admin
from .models import Device


class DeviceAdmin(admin.ModelAdmin):
    list_display = ["name", "company", "description", "address", "longitude", "latitude", "serialNumber"]
    search_filter = ["name", "company", "description", "address", "longitude", "latitude", "serialNumber"]
    list_filter = ["name", "company", "description", "address", "longitude", "latitude", "serialNumber"]


    class Meta:
        model = Device

admin.site.register(Device, DeviceAdmin)

