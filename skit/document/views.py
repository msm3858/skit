from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from .forms import MeetingDocumentForm, EmployeeDocumentForm
from .models import MeetingDocument, EmployeeDocument
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from django.contrib.auth import authenticate, login
from django.views.generic import View


class IndexView(generic.TemplateView):
    template_name = 'base/home.html'


class MeetingDocumentListView(generic.ListView):
    template_name = 'document/meeting_document_list.html'
    context_object_name = 'meeting_document_list'

    def get_queryset(self):
        return MeetingDocument.objects.all()


class MeetingDocumentDetailView(generic.DetailView):
    model = MeetingDocument
    template_name = 'document/meeting_document_detail.html'


class MeetingDocumentCreateView(CreateView):
    template_name = 'base/form.html.html'
    model = MeetingDocument
    form_class = MeetingDocumentForm
    # fields = ['', '', ''...]


class MeetingDocumentUpdateView(UpdateView):
    template_name = 'base/form.html.html'
    model = MeetingDocument
    form_class = MeetingDocumentForm


class MeetingDocumentDeleteView(DeleteView):
    model = MeetingDocument
    success_url = reverse_lazy('document:meeting_document_list')


class EmployeeDocumentListView(generic.ListView):
    template_name = 'document/employee_document_list.html'
    context_object_name = 'employee_document_list'

    def get_queryset(self):
        return MeetingDocument.objects.all()


class EmployeeDocumentDetailView(generic.DetailView):
    model = EmployeeDocument
    template_name = 'document/employee_document_detail.html'


class EmployeeDocumentCreateView(CreateView):
    template_name = 'base/form.html'
    model = EmployeeDocument
    form_class = EmployeeDocumentForm
    # fields = ['', '', ''...]


class EmployeeDocumentUpdateView(UpdateView):
    template_name = 'base/form.html'
    model = EmployeeDocument
    form_class = EmployeeDocumentForm


class EmployeeDocumentDeleteView(DeleteView):
    model = EmployeeDocument
    success_url = reverse_lazy('document:employee_document_list')
