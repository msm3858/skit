from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from .forms import EmployeeForm, FromMeetingAddMeetingParticipantForm, VisitorForm, RoomForm, MeetingForm, MeetingParticipantForm, \
    RoomReservationForm
from .models import Employee, Visitor, Room, Meeting, MeetingParticipant, RoomReservation


base_form = 'base/form.html'


class IndexView(generic.TemplateView):
    template_name = base_form


# Creating views for Employee
class EmployeeListView(generic.ListView):
    template_name = 'company/people/employee_list.html'
    context_object_name = 'employee_list'

    def get_queryset(self):
        return Employee.objects.all()


class EmployeeDetailView(generic.DetailView):
    model = Employee
    template_name = 'company/people/employee_detail.html'


class EmployeeCreateView(CreateView):
    template_name = base_form
    model = Employee
    form_class = EmployeeForm
    # fields = ['', '', ''...]


class EmployeeUpdateView(UpdateView):
    template_name = base_form
    model = Employee
    form_class = EmployeeForm


class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = reverse_lazy('company:employee_list')


# Creating views for Visitor
class VisitorListView(generic.ListView):
    template_name = 'company/people/visitor_list.html'
    context_object_name = 'visitor_list'

    def get_queryset(self):
        return Visitor.objects.all()


class VisitorDetailView(generic.DetailView):
    model = Visitor
    template_name = 'company/people/visitor_detail.html'


class VisitorCreateView(CreateView):
    template_name = base_form
    model = Visitor
    form_class = VisitorForm
    # fields = ['', '', ''...]


class VisitorUpdateView(UpdateView):
    template_name = base_form
    model = Visitor
    form_class = VisitorForm


class VisitorDeleteView(DeleteView):
    model = Visitor
    success_url = reverse_lazy('company:visitor_list')


# Creating views for Room
class RoomListView(generic.ListView):
    template_name = 'company/rooms/room_list.html'
    context_object_name = 'room_list'

    def get_queryset(self):
        return Room.objects.all()


class RoomDetailView(generic.DetailView):
    model = Room
    template_name = 'company/rooms/room_detail.html'


class RoomCreateView(CreateView):
    template_name = base_form
    model = Room
    form_class = RoomForm
    # fields = ['', '', ''...]


class RoomUpdateView(UpdateView):
    template_name = base_form
    model = Room
    form_class = RoomForm


class RoomDeleteView(DeleteView):
    model = Room
    success_url = reverse_lazy('company:room_list')


# Creating views for Meeting
class MeetingListView(generic.ListView):
    template_name = 'company/meeting/meeting_list.html'
    context_object_name = 'meeting_list'

    def get_queryset(self):
        return Meeting.objects.all()


class MeetingDetailView(generic.DetailView):
    model = Meeting
    template_name = 'company/meeting/meeting_detail.html'


class MeetingCreateView(CreateView):
    template_name = base_form
    model = Meeting
    form_class = MeetingForm
    # fields = ['', '', ''...]


class MeetingUpdateView(UpdateView):
    template_name = base_form
    model = Meeting
    form_class = MeetingForm


class MeetingDeleteView(DeleteView):
    model = Meeting
    success_url = reverse_lazy('company:meeting_list')


# Creating views for MeetingParticipant
class MeetingParticipantListView(generic.ListView):
    template_name = 'company/meeting/meeting_participant_list.html'
    context_object_name = 'meeting_participant_list'

    def get_queryset(self):
        return MeetingParticipant.objects.all()


class MeetingParticipantDetailView(generic.DetailView):
    model = MeetingParticipant
    template_name = 'company/meeting/meeting_participant_detail.html'


class MeetingParticipantCreateView(CreateView):
    template_name = base_form
    model = MeetingParticipant
    form_class = MeetingParticipantForm
    # fields = ['', '', ''...]


class FromMeetingAddMeetingParticipantCreateView(CreateView):
    template_name = 'company/meeting/form.html'
    model = MeetingParticipant
    form_class = FromMeetingAddMeetingParticipantForm
    success_url = reverse_lazy('company:meeting_list')
    # fields = ['', '', ''...]

    def dispatch(self, request, *args, **kwargs):
        """
        Overridden so we can make sure the `Meeting` instance exists
        before going any further.
        """
        self.meeting = get_object_or_404(Meeting, pk=kwargs['meeting_id'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """
        Overridden to add the ipsum relation to the `Lorem` instance.
        """
        form.instance.meeting = self.meeting
        return super().form_valid(form)


class MeetingParticipantUpdateView(UpdateView):
    template_name = base_form
    model = MeetingParticipant
    form_class = MeetingParticipantForm


class MeetingParticipantDeleteView(DeleteView):
    model = MeetingParticipant
    success_url = reverse_lazy('company:meeting_participant_list')


# Creating views for RoomReservation
class RoomReservationListView(generic.ListView):
    template_name = 'company/rooms/room_reservation_list.html'
    context_object_name = 'room_reservation_list'

    def get_queryset(self):
        return RoomReservation.objects.all()


class RoomReservationDetailView(generic.DetailView):
    model = RoomReservation
    template_name = 'company/rooms/room_reservation_detail.html'


class RoomReservationCreateView(CreateView):
    template_name = base_form
    model = RoomReservation
    form_class = RoomReservationForm
    # fields = ['', '', ''...]


class RoomReservationUpdateView(UpdateView):
    template_name = base_form
    model = RoomReservation
    form_class = RoomReservationForm


class RoomReservationDeleteView(DeleteView):
    model = RoomReservation
    success_url = reverse_lazy('company:room_reservation_list')
