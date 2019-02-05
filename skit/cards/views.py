from .forms import CardForm, EmployeeCardUsageForm, FreeEmployeeCardUsageForm, FreeVisitorCardUsageForm, \
    VisitorCardUsageForm
from .models import Card, EmployeeCardUsage, VisitorCardUsage
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy
from django.utils import timezone


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
    template_name = 'base/form.html'
    model = Card
    form_class = CardForm


class CardUpdateView(UpdateView):
    template_name = 'base/form.html'
    model = Card
    form_class = CardForm


class CardDeleteView(DeleteView):
    model = Card
    success_url = reverse_lazy('cards:card_list')


# Employee Card Usage views

# Views without modyfing.
class EmployeeCardUsageListView(generic.ListView):
    template_name = 'cards/employee_card_usage_list.html'
    context_object_name = 'card_usage_list'

    def get_queryset(self):
        return EmployeeCardUsage.objects.all()


class EmployeeCardUsageDetailView(generic.DetailView):
    model = EmployeeCardUsage
    template_name = 'cards/employee_cards_usage_detail.html'


# Views with modyfing.
class EmployeeCardUsageCreateView(CreateView):
    template_name = 'base/form.html'
    model = EmployeeCardUsage
    form_class = EmployeeCardUsageForm


class EmployeeCardUsageUpdateView(UpdateView):
    template_name = 'base/form.html'
    model = EmployeeCardUsage
    form_class = EmployeeCardUsageForm


class EmployeeCardUsageDeleteView(DeleteView):
    model = EmployeeCardUsage
    success_url = reverse_lazy('cards:employee_cards_usage_list')


class FormGiveEmployeeCardUsageUpdateView(FormView):
    template_name = 'base/form.html'
    form_class = FreeEmployeeCardUsageForm
    success_url = reverse_lazy('cards:employee_card_usage_list')

    def form_valid(self, form):
        form.fields['card'].queryset = Card.objects.filter(status='free')
        employee_card_usage = form.save(commit=False)
        employee_card_usage.start_time = timezone.localtime()
        card = Card.objects.get(pk=employee_card_usage.card.id)
        card.status = 'taken'
        card.save()
        employee_card_usage.save()
        return super().form_valid(form)


class TakeEmployeeCardUsageRedirectView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'cards:employee_card_usage_detail'

    def get_redirect_url(self, *args, **kwargs):
        employee_card_usage = EmployeeCardUsage.objects.get(id=kwargs['pk'])
        employee_card_usage.end_time = timezone.localtime()
        card = Card.objects.get(pk=employee_card_usage.card.id)
        card.status = 'free'
        card.save()
        employee_card_usage.save()
        return super().get_redirect_url(*args, **kwargs)


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
    template_name = 'base/form.html'
    model = VisitorCardUsage
    form_class = VisitorCardUsageForm


class VisitorCardUsageUpdateView(UpdateView):
    template_name = 'base/form.html'
    model = VisitorCardUsage
    form_class = VisitorCardUsageForm


class VisitorCardUsageDeleteView(DeleteView):
    model = VisitorCardUsage
    success_url = reverse_lazy('cards:visitor_cards_usage_list')


class FormGiveVisitorCardUsageUpdateView(FormView):
    template_name = 'base/form.html'
    form_class = FreeVisitorCardUsageForm
    success_url = reverse_lazy('cards:visitor_card_usage_list')

    def form_valid(self, form):
        form.fields['card'].queryset = Card.objects.filter(status='free')
        visitor_card_usage = form.save(commit=False)
        visitor_card_usage.start_time = timezone.localtime()
        card = Card.objects.get(pk=visitor_card_usage.card.id)
        card.status = 'taken'
        card.save()
        visitor_card_usage.save()
        return super().form_valid(form)


class TakeVisitorCardUsageRedirectView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'cards:visitor_card_usage_detail'

    def get_redirect_url(self, *args, **kwargs):
        visitor_card_usage = VisitorCardUsage.objects.get(id=kwargs['pk'])
        visitor_card_usage.end_time = timezone.localtime()
        card = Card.objects.get(pk=visitor_card_usage.card.id)
        card.status = 'free'
        card.save()
        visitor_card_usage.save()
        return super().get_redirect_url(*args, **kwargs)
