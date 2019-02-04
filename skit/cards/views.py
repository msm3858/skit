from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from .forms import CardForm, EmployeeCardUsageForm, VisitorCardUsageForm
from .models import Card, EmployeeCardUsage, VisitorCardUsage
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from django.contrib.auth import authenticate, login
from django.views.generic import View


# Index view
class IndexView(generic.TemplateView):
    template_name = 'base/home.html'


# Card views

class CardListView(generic.ListView):
    template_name = 'cards/card_list.html'
    context_object_name = 'card_list'

    def get_queryset(self):
        return Card.objects.all()


class FreeCardListView(generic.ListView):
    template_name = 'cards/card_list.html'
    context_object_name = 'card_list'

    def get_queryset(self):
        return Card.free.all()


class TakenCardListView(generic.ListView):
    template_name = 'cards/card_list.html'
    context_object_name = 'card_list'

    def get_queryset(self):
        return Card.taken.all()


class CardDetailView(generic.DetailView):
    model = Card
    template_name = 'cards/card_detail.html'


class CardCreateView(CreateView):
    template_name = 'cards/card_form.html'
    model = Card
    form_class = CardForm


class CardUpdateView(UpdateView):
    template_name = 'cards/card_form.html'
    model = Card
    form_class = CardForm


class CardDeleteView(DeleteView):
    model = Card
    success_url = reverse_lazy('cards:card_list')


# Employee Card Usage views

class EmployeeCardUsageListView(generic.ListView):
    template_name = 'cards/employee_cards_usage_list.html'
    context_object_name = 'employee_cards_usage_list'

    def get_queryset(self):
        return EmployeeCardUsage.objects.all()


class EmployeeCardUsageDetailView(generic.DetailView):
    model = EmployeeCardUsage
    template_name = 'cards/employee_cards_usage_detail.html'


class EmployeeCardUsageCreateView(CreateView):
    template_name = 'cards/employee_cards_usage_form.html'
    model = EmployeeCardUsage
    form_class = EmployeeCardUsageForm


class EmployeeCardUsageUpdateView(UpdateView):
    template_name = 'cards/employee_cards_usage_form.html'
    model = EmployeeCardUsage
    form_class = EmployeeCardUsageForm


class EmployeeCardUsageDeleteView(DeleteView):
    model = EmployeeCardUsage
    success_url = reverse_lazy('cards:employee_cards_usage_list')


class GiveEmployeeCardUsageUpdateView(UpdateView):
    model = EmployeeCardUsage
    fields = ('description', 'card', 'employee',)
    template_name = 'cards/employee_cards_usage_form.html'
    pk_url_kwarg = 'employee_card_usage_pk'
    context_object_name = 'employee_card_usage'

    def form_valid(self, form):
        employee_card_usage = form.save(commit=False)
        employee_card_usage.start_time.now()
        employee_card_usage.save()
        return redirect('cards:employee_cards_usage_detail', pk=employee_card_usage.uuid)


class TakeEmployeeCardUsageUpdateView(UpdateView):
    model = EmployeeCardUsage
    fields = ('description', 'card', 'employee',)
    template_name = 'cards/employee_cards_usage_form.html'
    pk_url_kwarg = 'employee_card_usage_pk'
    context_object_name = 'employee_card_usage'

    def form_valid(self, form):
        employee_card_usage = form.save(commit=False)
        employee_card_usage.end_time.now()
        employee_card_usage.save()
        return redirect('cards:employee_cards_usage_detail', pk=employee_card_usage.uuid)


# Visitor Card Usage views
class VisitorCardUsageListView(generic.ListView):
    template_name = 'cards/visitor_cards_usage_list.html'
    context_object_name = 'visitor_cards_usage_list'

    def get_queryset(self):
        return VisitorCardUsage.objects.all()


class VisitorCardUsageDetailView(generic.DetailView):
    model = VisitorCardUsage
    template_name = 'cards/visitor_cards_usage_detail.html'


class VisitorCardUsageCreateView(CreateView):
    template_name = 'cards/visitor_cards_usage_form.html'
    model = VisitorCardUsage
    form_class = VisitorCardUsageForm


class VisitorCardUsageUpdateView(UpdateView):
    template_name = 'cards/visitor_cards_usage_form.html'
    model = VisitorCardUsage
    form_class = VisitorCardUsageForm


class GiveVisitorCardUsageUpdateView(UpdateView):
    model = VisitorCardUsage
    fields = ('description', 'card', 'visitor',)
    template_name = 'cards/visitor_cards_usage_form.html'
    pk_url_kwarg = 'visitor_card_usage_pk'
    context_object_name = 'visitor_card_usage'

    def form_valid(self, form):
        visitor_card_usage = form.save(commit=False)
        visitor_card_usage.start_time.now()
        visitor_card_usage.save()
        return redirect('cards:visitor_cards_usage_detail', pk=visitor_card_usage.uuid)


class TakeVisitorCardUsageUpdateView(UpdateView):
    model = VisitorCardUsage
    fields = ('description', 'card', 'visitor',)
    template_name = 'cards/visitor_cards_usage_form.html'
    pk_url_kwarg = 'visitor_card_usage_pk'
    context_object_name = 'visitor_card_usage'

    def form_valid(self, form):
        visitor_card_usage = form.save(commit=False)
        visitor_card_usage.end_time.now()
        visitor_card_usage.save()
        return redirect('cards:visitor_cards_usage_detail', pk=visitor_card_usage.uuid)


class VisitorCardUsageDeleteView(DeleteView):
    model = VisitorCardUsage
    success_url = reverse_lazy('cards:visitor_cards_usage_list')
