# IMPORT DJANGO
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# IMPORT APPS PROJECT
from apps.administrator.models import BiddingVariable, BasicUsageRate
# IMPORT SELF APP
from .forms import TenderCalculationForm


class ProgiPixHome(TemplateView):
    """class that displays the main page

    Args:
        TemplateView: inherit a django class
    """
    template_name = 'bidding/home.html'

@method_decorator(csrf_exempt, name='dispatch')
class CalculateTenderTemplateView(TemplateView):
    """class that calculates the bids based on the configuration established in the database
    Args:
        The csrf token is canceled for practicality when evaluating.
        TemplateView: inherit a django class
    Returns:
        Eeturns a dictionary with all calculations segmented in a template
    """
    template_name = 'bidding/calculatetender.html'
    form_class = TenderCalculationForm
    model = BiddingVariable

    # send additional context
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form'] = self.form_class
        return context

    # table query BiddingVariable
    def get_bidding_variables(self):
        return self.model.objects.filter(is_active=True)
    
    # table query BasicUsageRate
    def get_basic_usage_rate(self):
        return BasicUsageRate.objects.get(pk=self.get_bidding_variables().values('basicusagerate')[0]['basicusagerate'])
    
    # get the active relations in the many to many PartnershipCostRange
    def get_partner_ship_cost_range(self):
        return self.get_bidding_variables()[0].partnershipcostranges.all()

    def calculate_basicuse(self, amount):
        """calculate the basic use rate and receive the entered amount
        Args:
            amount (float): the amount entered in the form
        Returns:
            float: returns the basic usage rate
        """
        bs = self.get_basic_usage_rate()
        percent = bs.percent
        minimum = bs.minimum
        maximum = bs.maximum
        baiscusecalculate = amount * (percent/100)
        if baiscusecalculate >= minimum and baiscusecalculate <= maximum:
            return baiscusecalculate
        else:
            return 0

    def calculate_association_cost(self, amount):
        """calculate the association_cost rate and receive the entered amount
        Args:
            amount (float): the amount entered in the form
        Returns:
            float: returns the association_cost
        """
        rangecost = self.get_partner_ship_cost_range()
        for r in rangecost:
            if amount >= r.minimum and amount <= r.maximum:
                return r.cost
            else:
                pass 
        return 0

    def calculation_total(self, amount):
        """father function that makes the calculations of the bids. This works called the post method
        Args:
            amount(float): the amount entered in the form
        Returns:
            dict: returns a dictionary with the rates
        """
        bv = self.get_bidding_variables()
        dic = {
            'basicusagerate' : self.calculate_basicuse(amount),
            'sellercommission' : bv[0].sellercommission,
            'partnershipcostrange' : self.calculate_association_cost(amount),
            'fixedstoragerate' : bv[0].fixedstoragerate,
        }
        taxesincluded = 0
        for key, value in dic.items():
            if type(value) is int or float:
                taxesincluded = taxesincluded + value 
        dic['taxesincluded'] = taxesincluded 
        dic['total'] = amount - taxesincluded           
        return dic

    def post(self, *args, **kwargs):
        """the post method is annulled, where functions are called 
           to calculate the bid and segment it into the different rates
        Returns:
            return a dictionary and a template
        """
        form = self.form_class(self.request.POST)
        if form.is_valid():
            calculationtotal = self.calculation_total(amount=form.cleaned_data['amount'])
            context = {
                'form' : self.form_class(self.request.POST),
                'basicusagerate': calculationtotal['basicusagerate'],
                'sellercommission' : calculationtotal['sellercommission'], 
                'partnershipcostrange' : calculationtotal['partnershipcostrange'],
                'fixedstoragerate' : calculationtotal['fixedstoragerate'],
                'taxesincluded': calculationtotal['taxesincluded'],
                'total' : calculationtotal['total'],
            }
            return render(self.request, self.template_name, context)
        else:
            return render(self.request, self.template_name, {'form' : form})

class DocsTemplateView(TemplateView):
    """class that displays the documentation for this project <3
    Args:
        TemplateView: inherit a django class
    """
    template_name = 'bidding/docs.html'