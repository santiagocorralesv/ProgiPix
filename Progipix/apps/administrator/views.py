# IMPORT DJANGO
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
# IMPORT SELF APP
from .models import BiddingVariable, BasicUsageRate
from .forms import BasicUsageRateForm

class HomeAdministratorView(TemplateView):
    template_name = 'administrator/home.html'

    def get_bidding_variables(self):
        return BiddingVariable.objects.get(is_active=True)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # bidding_variables = None
        # try:
        #     bidding_variables = self.get_bidding_variables()
        # except:
        context['basicuse'] = 150
        context['sellercommission'] = 100
        context['costrange'] = 100
        context['fixedrate'] = 100
        return context


class BasicUsageRateCreateView(CreateView):
    template_name = 'administrator/basicuse/basicuse.html'
    model = BasicUsageRate
    form_class = BasicUsageRateForm
    success_url = reverse_lazy('bidding:home-progipix')


class BasicUsageRateUpdateView(UpdateView):
    template_name = 'administrator/basicuse/basicuse.html'
    model = BasicUsageRate
    form_class = BasicUsageRateForm
    success_url = reverse_lazy('bidding:home-progipix')


class BasicUsageRateDeleteView(DeleteView):
    template_name = 'administrator/basicuse/delete.html'
    model = BasicUsageRate
    success_url = reverse_lazy('bidding:home-progipix')