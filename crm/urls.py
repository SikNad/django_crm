from django.urls import path
from . import views

urlpatterns = [
    # Услуги
    path('services/', views.ServiceListView.as_view(), name='service_list'),
    path('services/<int:pk>/', views.ServiceDetailView.as_view(), name='service_detail'),
    path('services/create/', views.ServiceCreateView.as_view(), name='service_create'),
    path('services/<int:pk>/update/', views.ServiceUpdateView.as_view(), name='service_update'),
    path('services/<int:pk>/delete/', views.ServiceDeleteView.as_view(), name='service_delete'),

    # Рекламные кампании
    path('campaigns/', views.CampaignListView.as_view(), name='campaign_list'),
    path('campaigns/<int:pk>/', views.CampaignDetailView.as_view(), name='campaign_detail'),
    path('campaigns/create/', views.CampaignCreateView.as_view(), name='campaign_create'),
    path('campaigns/<int:pk>/update/', views.CampaignUpdateView.as_view(), name='campaign_update'),
    path('campaigns/<int:pk>/delete/', views.CampaignDeleteView.as_view(), name='campaign_delete'),

    # Клиенты (Лиды)
    path('leads/', views.LeadListView.as_view(), name='lead_list'),
    path('leads/<int:pk>/', views.LeadDetailView.as_view(), name='lead_detail'),
    path('leads/create/', views.LeadCreateView.as_view(), name='lead_create'),
    path('leads/<int:pk>/update/', views.LeadUpdateView.as_view(), name='lead_update'),
    path('leads/<int:pk>/delete/', views.LeadDeleteView.as_view(), name='lead_delete'),

    # Контракты
    path('contracts/', views.ContractListView.as_view(), name='contract_list'),
    path('contracts/<int:pk>/', views.ContractDetailView.as_view(), name='contract_detail'),
    path('contracts/create/', views.ContractCreateView.as_view(), name='contract_create'),
    path('contracts/<int:pk>/update/', views.ContractUpdateView.as_view(), name='contract_update'),
    path('contracts/<int:pk>/delete/', views.ContractDeleteView.as_view(), name='contract_delete'),

    # Активные клиенты и перевод
    path('leads/<int:lead_id>/activate/', views.ActiveClientCreateView.as_view(), name='active_client_create'),
    path('active-clients/', views.ActiveClientListView.as_view(), name='activeclient_list'),
    path('active-clients/<int:pk>/', views.ActiveClientDetailView.as_view(), name='activeclient_detail'),

    path('statistics/', views.StatisticsView.as_view(), name='statistics'),
]
