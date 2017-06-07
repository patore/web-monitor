from django.contrib import admin
from .models import Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_filter = ["name"]
    list_filter = ["name"]

    class Meta:
        model = Company


admin.site.register(Company, CompanyAdmin)

