from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^home/', views.home, name='devices'),
    url(r'^device_data/', views.DeviceListView.as_view(), name='device_data'),
    url(r'^device_detail/(?P<slug>[\w-]+)/$', views.DeviceDetailView.as_view(), name='device_detail'),
]