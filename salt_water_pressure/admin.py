from django.contrib import admin
from .models import SaltWaterPressure


class SaltWaterPressureAdmin(admin.ModelAdmin):
    list_display = ["device", "reading", "timestamp"]
    search_filter = ["device", "reading", "timestamp"]
    list_filter = ["device", "reading", "timestamp"]

    class Meta:
        model = SaltWaterPressure

admin.site.register(SaltWaterPressure, SaltWaterPressureAdmin)