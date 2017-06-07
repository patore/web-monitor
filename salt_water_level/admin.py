from django.contrib import admin
from .models import SaltWaterLevel


class SaltWaterLevelAdmin(admin.ModelAdmin):
    list_display = ["device", "reading", "timestamp"]
    search_filter = ["device", "reading", "timestamp"]
    list_filter = ["device", "reading", "timestamp"]

    class Meta:
        model = SaltWaterLevel

admin.site.register(SaltWaterLevel, SaltWaterLevelAdmin)