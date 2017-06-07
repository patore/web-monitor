from django.contrib import admin
from .models import TubingPressure


class TubingPressureAdmin(admin.ModelAdmin):
    list_display = ["device", "reading", "timestamp"]
    search_filter = ["device", "reading", "timestamp"]
    list_filter = ["device", "reading", "timestamp"]

    class Meta:
        model = TubingPressure

admin.site.register(TubingPressure, TubingPressureAdmin)