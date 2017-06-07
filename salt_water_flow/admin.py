from django.contrib import admin
from .models import SaltWaterFlow


class SaltWaterFlowAdmin(admin.ModelAdmin):
    list_display = ["device", "reading", "timestamp"]
    search_filter = ["device", "reading", "timestamp"]
    list_filter = ["device", "reading", "timestamp"]

    class Meta:
        model = SaltWaterFlow

admin.site.register(SaltWaterFlow, SaltWaterFlowAdmin)