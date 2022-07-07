# IMPORT DJANGO
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# IMPORT SELF APP
from .models import BasicUsageRate, PartnershipCostRange, BiddingVariable
from .forms import BasicUsageRateForm, BiddingVariableForm, PartnershipCostRangeForm

class HomeAdministratorView(TemplateView):
    """class that returns a template for the admin home page with a query to the BiddingVariable table
    Args:
        TemplateView: inherit a django class
    Returns:
        Template
    """
    template_name = 'administrator/home.html'

    # table query BiddingVariable
    def get_bidding_variables(self):
        return BiddingVariable.objects.all()

    # additional context sending
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['biddingvariable'] = self.get_bidding_variables()
        return context


@method_decorator(csrf_exempt, name='dispatch')
class BiddingVariableCreateView(CreateView):
    """class to create record in database from table BiddingVariable
    Args:
        The csrf token is canceled for practicality when evaluating.
        CreateView: inherit a django class
    Returns:
        Record creation
    """
    template_name = 'administrator/biddingvariable/biddingvariable.html'
    model = BiddingVariable
    form_class = BiddingVariableForm
    success_url = reverse_lazy('administrator:administrator-home')

    # table query BiddingVariable
    def get_basic_usage_rate(self):
        return BasicUsageRate.objects.all()

    # table query PartnershipCostRange
    def get_partner_ship_cost_range(self):
        return PartnershipCostRange.objects.all()

    # additional context sending
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['basicusagerate'] = self.get_basic_usage_rate()
        context['partnershipcostrange'] = self.get_partner_ship_cost_range()
        return context

@method_decorator(csrf_exempt, name='dispatch')
class BiddingVariableUpdateView(UpdateView):
    """class to create an update in the database from the BiddingVariable
    Args:
        The csrf token is canceled for practicality when evaluating.
        UpdateView: inherit a django class
    Returns:
        Record update
    """
    template_name = 'administrator/biddingvariable/biddingvariable.html'
    model = BiddingVariable
    form_class = BiddingVariableForm
    success_url = reverse_lazy('administrator:administrator-home')

    # table query BasicUsageRate
    def get_basic_usage_rate(self):
        return BasicUsageRate.objects.all()

    # table query PartnershipCostRange
    def get_partner_ship_cost_range(self):
        return PartnershipCostRange.objects.all()

    # additional context sending
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['basicusagerate'] = self.get_basic_usage_rate()
        context['partnershipcostrange'] = self.get_partner_ship_cost_range()
        return context


@method_decorator(csrf_exempt, name='dispatch')
class BasicUsageRateCreateView(CreateView):
    """class to create a record in the database from BasicUsageRate
    Args:
        The csrf token is canceled for practicality when evaluating.    
        CreateView: inherit a django class
    Returns:
        Record creation
    """
    template_name = 'administrator/basicuse/basicusageratecreate.html'
    model = BasicUsageRate
    form_class = BasicUsageRateForm
    success_url = reverse_lazy('bidding:home-progipix')

    # override post method to get record creation by ajax. returning a json response
    def post(self, request, *args, **kwargs):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                response = JsonResponse({'message': 'Good job'})
                response.status_code = 201
                return response
            else:
                response = JsonResponse({'message': 'error'})
                response.status_code = 400
                return response
        else:
            return self.success_url


@method_decorator(csrf_exempt, name='dispatch')
class BasicUsageRateUpdateView(UpdateView):
    """class to update a record in the database from BasicUsageRate
    Args:
        The csrf token is canceled for practicality when evaluating.
        UpdateView: inherit a django class
    Returns:
        Record update
    """
    template_name = 'administrator/basicuse/basicusagerateupdate.html'
    model = BasicUsageRate
    form_class = BasicUsageRateForm
    success_url = reverse_lazy('administrator:administrator-home')

    # additional context sending
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['object'] = self.kwargs['pk']
        return context

    # override post method to get record creation by ajax. returning a json response
    def post(self, request, *args, **kwargs):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():
                form.save()
                response = JsonResponse({'message': 'Good job'})
                response.status_code = 201
                return response
            else:
                response = JsonResponse({'message': 'error'})
                response.status_code = 400
                return response
        else:
            return self.success_url

@method_decorator(csrf_exempt, name='dispatch')
class BasicUsageRateDeleteView(DeleteView):
    """class to delete a record in the database from BasicUsageRate

    Args:
        The csrf token is canceled for practicality when evaluating.
        DeleteView: inherit a django class
    Returns:
        Record delete
    """
    template_name = 'administrator/basicuse/basicusageratedelete.html'
    model = BasicUsageRate
    success_url = reverse_lazy('administrator:administrator-home')
    
    # the dispatch method is annulled to send the object instance to the template
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    # override post method to get record creation by ajax. returning a json response
    def post(self, request, *args, **kwargs):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            self.object.delete()
            response = JsonResponse({'message': 'Good job!'})
            response.status_code = 201
            return response
        else:
            return self.success_url


@method_decorator(csrf_exempt, name='dispatch')
class PartnershipCostRangeCreateView(CreateView):
    """class to create a record in the database from BasicUsageRate
    Args:
        The csrf token is canceled for practicality when evaluating.
        CreateView: inherit a django class
    Returns:
        Record creation
    """
    template_name = 'administrator/partnershipcostrange/partnershipcostrangecreate.html'
    model = PartnershipCostRange
    form_class = PartnershipCostRangeForm
    success_url = reverse_lazy('administrator:administrator-home')

    # override post method to get record creation by ajax. returning a json response
    def post(self, request, *args, **kwargs):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                response = JsonResponse({'message': 'Good job'})
                response.status_code = 201
                return response
            else:
                response = JsonResponse({'message': 'error'})
                response.status_code = 400
                return response
        else:
            return self.success_url


@method_decorator(csrf_exempt, name='dispatch')
class PartnershipCostRangeUpdateView(UpdateView):
    """class to update a record in the database from BasicUsageRate

    Args:
        The csrf token is canceled for practicality when evaluating.
        UpdateView: inherit a django class
    Returns:
        Record update
    """
    template_name = 'administrator/partnershipcostrange/partnershipcostrangeupdate.html'
    model = PartnershipCostRange
    form_class = PartnershipCostRangeForm
    success_url = reverse_lazy('administrator:administrator-home')

    # additional context sending
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['object'] = self.kwargs['pk']
        return context

    # override post method to get record creation by ajax. returning a json response
    def post(self, request, *args, **kwargs):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():
                form.save()
                response = JsonResponse({'message': 'Good job'})
                response.status_code = 201
                return response
            else:
                response = JsonResponse({'message': 'error'})
                response.status_code = 400
                return response
        else:
            return self.success_url

@method_decorator(csrf_exempt, name='dispatch')
class PartnershipCostRangeDeleteView(DeleteView):
    """class to delete a record in the database from BasicUsageRate
    Args:
        The csrf token is canceled for practicality when evaluating.
        DeleteView: inherit a django class
    Returns:
        Record delete
    """
    template_name = 'administrator/partnershipcostrange/partnershipcostrangedelete.html'
    model = PartnershipCostRange
    form_class = PartnershipCostRangeForm
    success_url = reverse_lazy('administrator:administrator-home')

    # the dispatch method is annulled to send the object instance to the template
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    # override post method to get record creation by ajax. returning a json response
    def post(self, request, *args, **kwargs):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            self.object.delete()
            response = JsonResponse({'message': 'Good job!'})
            response.status_code = 201
            return response
        else:
            return self.success_url