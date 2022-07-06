# IMPORT DJANGO
from django.urls import path
# IMPORT SELF APP
from .views import ProgiPixHome, CalculateTenderTemplateView, DocsTemplateView

app_name = 'bidding'

urlpatterns = [
    path('', ProgiPixHome.as_view(), name='home-bidding'),
    path('calculate-tender', CalculateTenderTemplateView.as_view(), name='calculate-tender'),
    path('docs', DocsTemplateView.as_view(), name='docs'),
]
