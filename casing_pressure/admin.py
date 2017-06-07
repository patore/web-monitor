from django.contrib import admin
from .models import CasingPressure


class CasingPressureAdmin(admin.ModelAdmin):
    list_display = ["device", "reading", "timestamp"]
    search_filter = ["device", "reading", "timestamp"]
    list_filter = ["device", "reading", "timestamp"]

    class Meta:
        model = CasingPressure

admin.site.register(CasingPressure, CasingPressureAdmin)