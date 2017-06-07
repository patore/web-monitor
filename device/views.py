from django.shortcuts import render
from django.http import JsonResponse
from .models import Device
from casing_pressure.models import CasingPressure
from oil_level.models import OilLevel
from salt_water_level.models import SaltWaterLevel
from salt_water_flow.models import SaltWaterFlow
from salt_water_pressure.models import SaltWaterPressure
from tubing_pressure.models import TubingPressure
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


def home(request):

    return render(request, "device/device_dashboard.html")


class DeviceListView(ListView):
    model = Device
    template_name = "device/device_dashboard.html"


class DeviceDetailView(DetailView):
    model = Device
    template_name = "device/device_detail.html"

    def get_context_data(self, **kwargs):
        context = super(DeviceDetailView, self).get_context_data(**kwargs)
        device = Device.objects.filter(slug__iexact=self.kwargs['slug'])
        casingPressure = CasingPressure.objects.filter(device=device)
        oilLevel = OilLevel.objects.filter(device=device)
        saltWaterPressure = SaltWaterPressure.objects.filter(device=device)
        saltWaterFlow = SaltWaterFlow.objects.filter(device=device)
        saltWaterLevel = SaltWaterLevel.objects.filter(device=device)
        tubingPressure = TubingPressure.objects.filter(device=device)
        context['casing_pressure'] = casingPressure
        context['oil_level'] = oilLevel
        context['salt_water_pressure'] = saltWaterPressure
        context['salt_water_flow'] = saltWaterFlow
        context['salt_water_level'] = saltWaterLevel
        context['tubing_pressure'] = tubingPressure
        return context