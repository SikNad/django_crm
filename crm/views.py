from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.db.models import Sum
from .models import Service, Campaign, Lead, ActiveClient, Contract
from .mixins import RoleRequiredMixin


# ==========================================
# CRUD ДЛЯ УСЛУГ (Маркетолог)
# ==========================================

class ServiceListView(RoleRequiredMixin, ListView):
    model = Service
    template_name = 'crm/service_list.html'
    context_object_name = 'services'
    allowed_roles = ['Маркетолог']


class ServiceDetailView(RoleRequiredMixin, DetailView):
    model = Service
    template_name = 'crm/service_detail.html'
    allowed_roles = ['Маркетолог']


class ServiceCreateView(RoleRequiredMixin, CreateView):
    model = Service
    template_name = 'crm/service_form.html'
    fields = ['title', 'description', 'price']
    success_url = reverse_lazy('service_list')
    allowed_roles = ['Маркетолог']


class ServiceUpdateView(RoleRequiredMixin, UpdateView):
    model = Service
    template_name = 'crm/service_form.html'
    fields = ['title', 'description', 'price']
    success_url = reverse_lazy('service_list')
    allowed_roles = ['Маркетолог']


class ServiceDeleteView(RoleRequiredMixin, DeleteView):
    model = Service
    template_name = 'crm/service_confirm_delete.html'
    success_url = reverse_lazy('service_list')
    allowed_roles = ['Маркетолог']


# ==========================================
# CRUD ДЛЯ РЕКЛАМНЫХ КАМПАНИЙ (Маркетолог)
# ==========================================

class CampaignListView(RoleRequiredMixin, ListView):
    model = Campaign
    template_name = 'crm/campaign_list.html'
    context_object_name = 'campaigns'
    allowed_roles = ['Маркетолог']


class CampaignDetailView(RoleRequiredMixin, DetailView):
    model = Campaign
    template_name = 'crm/campaign_detail.html'
    allowed_roles = ['Маркетолог']


class CampaignCreateView(RoleRequiredMixin, CreateView):
    model = Campaign
    template_name = 'crm/campaign_form.html'
    fields = ['title', 'service', 'channel', 'budget']
    success_url = reverse_lazy('campaign_list')
    allowed_roles = ['Маркетолог']


class CampaignUpdateView(RoleRequiredMixin, UpdateView):
    model = Campaign
    template_name = 'crm/campaign_form.html'
    fields = ['title', 'service', 'channel', 'budget']
    success_url = reverse_lazy('campaign_list')
    allowed_roles = ['Маркетолог']


class CampaignDeleteView(RoleRequiredMixin, DeleteView):
    model = Campaign
    template_name = 'crm/campaign_confirm_delete.html'
    success_url = reverse_lazy('campaign_list')
    allowed_roles = ['Маркетолог']


# ==========================================
# CRUD ДЛЯ ПОТЕНЦИАЛЬНЫХ КЛИЕНТОВ (Оператор, Менеджер)
# ==========================================

class LeadListView(RoleRequiredMixin, ListView):
    model = Lead
    template_name = 'crm/lead_list.html'
    context_object_name = 'leads'
    allowed_roles = ['Оператор', 'Менеджер']


class LeadDetailView(RoleRequiredMixin, DetailView):
    model = Lead
    template_name = 'crm/lead_detail.html'
    allowed_roles = ['Оператор', 'Менеджер']


class LeadCreateView(RoleRequiredMixin, CreateView):
    model = Lead
    template_name = 'crm/lead_form.html'
    fields = ['full_name', 'phone', 'email', 'campaign']
    success_url = reverse_lazy('lead_list')
    allowed_roles = ['Оператор', 'Менеджер']


class LeadUpdateView(RoleRequiredMixin, UpdateView):
    model = Lead
    template_name = 'crm/lead_form.html'
    fields = ['full_name', 'phone', 'email', 'campaign']
    success_url = reverse_lazy('lead_list')
    allowed_roles = ['Оператор', 'Менеджер']


class LeadDeleteView(RoleRequiredMixin, DeleteView):
    model = Lead
    template_name = 'crm/lead_confirm_delete.html'
    success_url = reverse_lazy('lead_list')
    allowed_roles = ['Оператор', 'Менеджер']


# ==========================================
# КОНТРАКТЫ (Менеджер)
# ==========================================

class ContractListView(RoleRequiredMixin, ListView):
    model = Contract
    template_name = 'crm/contract_list.html'
    context_object_name = 'contracts'
    allowed_roles = ['Менеджер']


class ContractDetailView(RoleRequiredMixin, DetailView):
    model = Contract
    template_name = 'crm/contract_detail.html'
    allowed_roles = ['Менеджер']


class ContractCreateView(RoleRequiredMixin, CreateView):
    model = Contract
    template_name = 'crm/contract_form.html'
    fields = ['title', 'service', 'document', 'date_signed', 'duration', 'amount']
    success_url = reverse_lazy('contract_list')
    allowed_roles = ['Менеджер']


class ContractUpdateView(RoleRequiredMixin, UpdateView):
    model = Contract
    template_name = 'crm/contract_form.html'
    fields = ['title', 'service', 'document', 'date_signed', 'duration', 'amount']
    success_url = reverse_lazy('contract_list')
    allowed_roles = ['Менеджер']


class ContractDeleteView(RoleRequiredMixin, DeleteView):
    model = Contract
    template_name = 'crm/contract_confirm_delete.html'
    success_url = reverse_lazy('contract_list')
    allowed_roles = ['Менеджер']


# ==========================================
# ПЕРЕВОД В АКТИВНОГО КЛИЕНТА И ПРОСМОТР (Менеджер)
# ==========================================

class ActiveClientCreateView(RoleRequiredMixin, CreateView):
    model = ActiveClient
    template_name = 'crm/activeclient_form.html'
    fields = ['contract']
    allowed_roles = ['Менеджер']

    def dispatch(self, request, *args, **kwargs):
        self.lead = get_object_or_404(Lead, pk=self.kwargs['lead_id'])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lead'] = self.lead
        return context

    def form_valid(self, form):
        form.instance.lead = self.lead
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('lead_list')


class ActiveClientListView(RoleRequiredMixin, ListView):
    model = ActiveClient
    template_name = 'crm/activeclient_list.html'
    context_object_name = 'active_clients'
    allowed_roles = ['Менеджер', 'Администратор']


class ActiveClientDetailView(RoleRequiredMixin, DetailView):
    model = ActiveClient
    template_name = 'crm/activeclient_detail.html'
    allowed_roles = ['Менеджер', 'Администратор']


# ==========================================
# СТАТИСТИКА (Все роли)
# ==========================================

class StatisticsView(RoleRequiredMixin, ListView):
    model = Campaign
    template_name = 'crm/statistics.html'
    context_object_name = 'campaigns'
    allowed_roles = ['Администратор', 'Оператор', 'Маркетолог', 'Менеджер']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stats = []
        for campaign in Campaign.objects.all():
            leads_count = campaign.leads.count()
            active_count = ActiveClient.objects.filter(lead__campaign=campaign).count()

            # Доход: сумма контрактов активных клиентов этой кампании
            income = Contract.objects.filter(active_client__lead__campaign=campaign).aggregate(total=Sum('amount'))[
                         'total'] or 0
            budget = campaign.budget

            stats.append({
                'campaign': campaign,
                'leads_count': leads_count,
                'active_count': active_count,
                'income': income,
                'budget': budget,
            })
        context['stats'] = stats
        return context
