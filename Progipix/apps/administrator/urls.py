# IMPORT DJANGO
from django.urls import path
# IMPORT SELF APP
from .views import HomeAdministratorView, BasicUsageRateCreateView, BasicUsageRateUpdateView, BasicUsageRateDeleteView, \
    BiddingVariableCreateView, BiddingVariableUpdateView, PartnershipCostRangeCreateView, PartnershipCostRangeUpdateView, \
    PartnershipCostRangeDeleteView

app_name = 'administrator'

urlpatterns = [
    path('home-administrator', HomeAdministratorView.as_view(), name='administrator-home'),

    path('biddingvariable-create', BiddingVariableCreateView.as_view(), name='biddingvariable-create'),
    path('biddingvariable-update/<pk>', BiddingVariableUpdateView.as_view(), name='biddingvariable-update'),
    
    path('basic-usage-rate-create', BasicUsageRateCreateView.as_view(), name='basic-usage-rate-create'),
    path('basic-usage-rate-update/<pk>', BasicUsageRateUpdateView.as_view(), name='basic-usage-rate-update'),
    path('basic-usage-rate-delete/<pk>', BasicUsageRateDeleteView.as_view(), name='basic-usage-rate-delete'),

    path('partner-ship-cost-range-create', PartnershipCostRangeCreateView.as_view(), name='partner-ship-cost-range-create'),
    path('partner-ship-cost-range-update/<pk>', PartnershipCostRangeUpdateView.as_view(), name='partner-ship-cost-range-update'),
    path('partner-ship-cost-range-delete/<pk>', PartnershipCostRangeDeleteView.as_view(), name='partner-ship-cost-range-delete'),
]
