# IMPORT DJANGO
from django import forms
# IMPORT APPS PROJECT
from apps.administrator.models import BiddingCalculation

class TenderCalculationForm(forms.ModelForm):
    class Meta:
        model = BiddingCalculation
        fields = ('amount',)
        widgets = {
            'amount': forms.NumberInput(attrs={'class' : 'form-control rounded-3'})
        }
        help_texts = {
            'amount' : 'Enter your amount'
        }
