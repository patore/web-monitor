from django.contrib import admin
from .models import OilLevel


class OilLevelAdmin(admin.ModelAdmin):
    list_display = ["device", "reading", "timestamp"]
    search_filter = ["device", "reading", "timestamp"]
    list_filter = ["device", "reading", "timestamp"]

    class Meta:
        model = OilLevel

admin.site.register(OilLevel, OilLevelAdmin)