from django.db import models
from device.models import Device


class SaltWaterPressure(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    reading = models.CharField(max_length=200, unique=True, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.reading