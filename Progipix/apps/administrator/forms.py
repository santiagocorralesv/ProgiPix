# IMPORT DJANGO
from django import forms

# IMPORT SELF APP
from .models import BasicUsageRate

class BasicUsageRateForm(forms.ModelForm):
    class Meta:
        model = BasicUsageRate
        fields = ('percent', 'minimum', 'maximum', )