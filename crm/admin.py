from django.contrib import admin
from .models import Service, Campaign, Lead, Contract, ActiveClient


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('title', 'service', 'channel', 'budget')


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'email', 'campaign')


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('title', 'service', 'date_signed', 'amount')


@admin.register(ActiveClient)
class ActiveClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'lead', 'contract')

