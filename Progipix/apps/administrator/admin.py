# IMPORT DJANGO
from django.contrib import admin

# IMPORT SELF APP
from .models import BasicUsageRate, PartnershipCostRange, BiddingVariable, BiddingCalculation
# Register your models here.

admin.site.register(BasicUsageRate)
admin.site.register(PartnershipCostRange)
admin.site.register(BiddingVariable)
admin.site.register(BiddingCalculation)