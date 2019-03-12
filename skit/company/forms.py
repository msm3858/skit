from .models import Employee, Visitor, Room, Meeting, MeetingParticipant, RoomReservation
from django import forms
from bootstrap_datepicker_plus import DateTimePickerInput


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'last_name', 'department', 'position']
        labels = {
            'name': 'Imię',
            'last_name': 'Nazwisko',
            'department': 'Dział',
            'position': 'Stanowisko',

        }


class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['name', 'last_name', 'purpose_of_visit', 'employee', 'description', ]
        labels = {
            'name': 'Imię',
            'last_name': 'Nazwisko',
            'purpose_of_visit': 'Cel wizyty',
            'employee': 'Opiekun(pracownik odpowiedzialny)',
            'description': 'Opis(opcjonalnie)',
        }
        widgets = {
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 5}),

        }


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'capacity', 'stuff', ]
        labels = {
            'name': 'Numer pokoju',
            'capacity': 'Pojemność(ilość miejsc)',
            'stuff': 'Wyposażenie',
        }

    widgets = {
        'stuff': forms.Textarea(attrs={'cols': 60, 'rows': 5}),

    }


class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['description', 'number_of_participants', 'kind', ]
        labels = {
            'description': 'Opis konferencji',
            'number_of_participants': 'Ilość uczestników',
            'kind': 'Rodzaj konferencji',
        }

        widgets = {
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 5}),
        }


class MeetingParticipantForm(forms.ModelForm):
    class Meta:
        model = MeetingParticipant
        fields = ['meeting', 'visitors', 'employees', ]
        labels = {
            'meeting': 'Spotkanie',
            'visitors': 'Goście',
            'employees': 'Pracownicy',
        }
class FromMeetingAddMeetingParticipantForm(forms.ModelForm):
    class Meta:
        model = MeetingParticipant
        fields = ['visitors', 'employees', ]
        labels = {
            'visitors': 'Goście',
            'employees': 'Pracownicy',
        }

class RoomReservationForm(forms.ModelForm):
    class Meta:
        model = RoomReservation
        fields = ['room', 'meeting', 'start_time', 'end_time', 'reserved_by']
        labels = {
            'room': 'Numer pokoju',
            'meeting': 'Spotkanie',
            'start_time': 'Początek rezerwacji',
            'end_time': 'Koniec rezerwacji',
            'reserved_by': 'Zarezerwowane przez..',
        }
        widgets = {
            'start_time': DateTimePickerInput(),
            'end_time': DateTimePickerInput(),
        }


