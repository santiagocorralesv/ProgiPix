# IMPORT DJANGO
from django.urls import path
# IMPORT SELF APP
from .views import HomeAdministratorView, BasicUsageRateCreateView, BasicUsageRateUpdateView, BasicUsageRateDeleteView

app_name = 'administrator'

urlpatterns = [
    path('home-administrator', HomeAdministratorView.as_view(), name='administrator-home'),
    path('basic-usage-rate-create', BasicUsageRateCreateView.as_view(), name='basic-usage-rate-create'),
    path('basic-usage-rate-update/<pk>', BasicUsageRateUpdateView.as_view(), name='basic-usage-rate-update'),
    path('basic-usage-rate-delete/<pk>', BasicUsageRateDeleteView.as_view(), name='basic-usage-rate-delete'),
]
