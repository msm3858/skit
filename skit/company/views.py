from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from .forms import EmployeeForm, VisitorForm, RoomForm, CardUsageForm, MeetingForm, MeetingParticipantForm, \
    RoomReservationForm
from .models import Employee, Visitor, Room, CardUsage, Meeting, MeetingParticipant, RoomReservation
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from django.contrib.auth import authenticate, login
from django.views.generic import View

from django.contrib.auth.decorators import login_required


class IndexView(generic.TemplateView):
    template_name = 'base/home.html'


# Creating views for Employee
class EmployeeListView(generic.ListView):
    template_name = 'company/employee_list.html'
    context_object_name = 'employee_list'

    def get_queryset(self):
        return Employee.objects.all()


class EmployeeDetailView(generic.DetailView):
    model = Employee
    template_name = 'company/employee_detail.html'


class EmployeeCreateView(CreateView):
    template_name = 'company/employee_form.html'
    model = Employee
    form_class = EmployeeForm
    # fields = ['', '', ''...]


class EmployeeUpdateView(UpdateView):
    template_name = 'company/employee_form.html'
    model = Employee
    form_class = EmployeeForm


class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = reverse_lazy('company:employee_list')


# Creating views for Visitor
class VisitorListView(generic.ListView):
    template_name = 'company/visitor_list.html'
    context_object_name = 'visitor_list'

    def get_queryset(self):
        return Visitor.objects.all()


class VisitorDetailView(generic.DetailView):
    model = Visitor
    template_name = 'company/visitor_detail.html'


class VisitorCreateView(CreateView):
    template_name = 'company/visitor_form.html'
    model = Visitor
    form_class = VisitorForm
    # fields = ['', '', ''...]


class VisitorUpdateView(UpdateView):
    template_name = 'company/visitor_form.html'
    model = Visitor
    form_class = VisitorForm


class VisitorDeleteView(DeleteView):
    model = Visitor
    success_url = reverse_lazy('company:visitor_list')


# Creating views for Room
class RoomListView(generic.ListView):
    template_name = 'company/room_list.html'
    context_object_name = 'room_list'

    def get_queryset(self):
        return Room.objects.all()


class RoomDetailView(generic.DetailView):
    model = Room
    template_name = 'company/room_detail.html'


class RoomCreateView(CreateView):
    template_name = 'company/room_form.html'
    model = Room
    form_class = RoomForm
    # fields = ['', '', ''...]


class RoomUpdateView(UpdateView):
    template_name = 'company/room_form.html'
    model = Room
    form_class = RoomForm


class RoomDeleteView(DeleteView):
    model = Room
    success_url = reverse_lazy('company:room_list')


# Creating views for CardUsage
class CardUsageListView(generic.ListView):
    template_name = 'company/card_usage_list.html'
    context_object_name = 'card_usage_list'

    def get_queryset(self):
        return CardUsage.objects.all()


class CardUsageDetailView(generic.DetailView):
    model = CardUsage
    template_name = 'company/card_usage_detail.html'


class CardUsageCreateView(CreateView):
    template_name = 'company/card_usage_form.html'
    model = CardUsage
    form_class = CardUsageForm
    # fields = ['', '', ''...]


class CardUsageUpdateView(UpdateView):
    template_name = 'company/card_usage_form.html'
    model = CardUsage
    form_class = CardUsageForm


class CardUsageDeleteView(DeleteView):
    model = CardUsage
    success_url = reverse_lazy('company:card_usage_list')


# Creating views for Meeting
class MeetingListView(generic.ListView):
    template_name = 'company/meeting_list.html'
    context_object_name = 'meeting_list'

    def get_queryset(self):
        return Meeting.objects.all()


class MeetingDetailView(generic.DetailView):
    model = Meeting
    template_name = 'company/meeting_detail.html'


class MeetingCreateView(CreateView):
    template_name = 'company/meeting_form.html'
    model = Meeting
    form_class = MeetingForm
    # fields = ['', '', ''...]


class MeetingUpdateView(UpdateView):
    template_name = 'company/meeting_form.html'
    model = Meeting
    form_class = MeetingForm


class MeetingDeleteView(DeleteView):
    model = Meeting
    success_url = reverse_lazy('company:meeting_list')


# Creating views for MeetingParticipant
class MeetingParticipantListView(generic.ListView):
    template_name = 'company/meeting_participant_list.html'
    context_object_name = 'meeting_participant_list'

    def get_queryset(self):
        return MeetingParticipant.objects.all()


class MeetingParticipantDetailView(generic.DetailView):
    model = MeetingParticipant
    template_name = 'company/meeting_participant_detail.html'


class MeetingParticipantCreateView(CreateView):
    template_name = 'company/meeting_participant_form.html'
    model = MeetingParticipant
    form_class = MeetingParticipantForm
    # fields = ['', '', ''...]


class MeetingParticipantUpdateView(UpdateView):
    template_name = 'company/meeting_participant_form.html'
    model = MeetingParticipant
    form_class = MeetingParticipantForm


class MeetingParticipantDeleteView(DeleteView):
    model = MeetingParticipant
    success_url = reverse_lazy('company:meeting_participant_list')


# Creating views for RoomReservation
class RoomReservationListView(generic.ListView):
    template_name = 'company/room_reservation_list.html'
    context_object_name = 'room_reservation_list'

    def get_queryset(self):
        return RoomReservation.objects.all()


class RoomReservationDetailView(generic.DetailView):
    model = RoomReservation
    template_name = 'company/room_reservation_detail.html'


class RoomReservationCreateView(CreateView):
    template_name = 'company/room_reservation_form.html'
    model = RoomReservation
    form_class = RoomReservationForm
    # fields = ['', '', ''...]


class RoomReservationUpdateView(UpdateView):
    template_name = 'company/room_reservation_form.html'
    model = RoomReservation
    form_class = RoomReservationForm


class RoomReservationDeleteView(DeleteView):
    model = RoomReservation
    success_url = reverse_lazy('company:room_reservation_list')
