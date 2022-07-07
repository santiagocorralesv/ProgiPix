# IMPORT DJANGO
from django import forms
# IMPORT SELF APP
from .models import BasicUsageRate, BiddingVariable, PartnershipCostRange


# form to create or update model records BasicUsageRate
class BasicUsageRateForm(forms.ModelForm):
    class Meta:
        model = BasicUsageRate
        fields = ('percent', 'minimum', 'maximum', )


# form to create or update model records BiddingVariable
class BiddingVariableForm(forms.ModelForm):
    class Meta:
        model = BiddingVariable
        fields = ('is_active', 'basicusagerate', 'sellercommission', 'fixedstoragerate', 'partnershipcostranges', )
        widgets = {
            'is_active' : forms.CheckboxInput(),
            'basicusagerate' : forms.Select(attrs={'class': 'form-control'}),
            'sellercommission' : forms.NumberInput(attrs={'class': 'form-control'}),
            'fixedstoragerate' : forms.NumberInput(attrs={'class': 'form-control'}),
            'partnershipcostranges' : forms.SelectMultiple(attrs={'class': 'form-control select2'}),
        }
        labels = {
            'is_active' : 'Is active', 
            'basicusagerate' : 'Basic usage rate',
            'sellercommission' : 'Seller commission',
            'fixedstoragerate' : 'Fixed storage rate',
            'partnershipcostranges' : 'Partner ship cost ranges'
        }


# form to create or update model records PartnershipCostRange
class PartnershipCostRangeForm(forms.ModelForm):
    class Meta:
        model = PartnershipCostRange
        fields = ('cost', 'minimum', 'maximum', )
        widgets = {
            'cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'minimum' : forms.NumberInput(attrs={'class': 'form-control'}),
            'maximum' : forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'cost': 'Cost',
            'minimum' : 'Minimun',
            'maximum' : 'Maximum',
        }