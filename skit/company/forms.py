from .models import Employee, Visitor, Room, CardUsage, Meeting, MeetingParticipant, RoomReservation
from django import forms

from django.contrib.auth.models import User


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


class CardUsageForm(forms.ModelForm):
    class Meta:
        model = CardUsage
        fields = ['description', 'start_time', 'end_time', ]
        labels = {
            'description': 'Opis(opcjonalne)',
            'start_time': 'Początek',
            'end_time': 'Koniec',
        }

        widgets = {
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 5}),
            'start_time': forms.SelectDateWidget(),
            'end_time': forms.SelectDateWidget(),

        }


class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['description', 'number_of_participants', 'kind', ]
        labels = {
            'description': 'Numer pokoju',
            'number_of_participants': 'Ilość uczestników',
            'kind': 'Rodzaj spotkania',
        }

        widgets = {
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 5}),
        }


class MeetingParticipantForm(forms.ModelForm):
    class Meta:
        model = MeetingParticipant
        fields = ['meeting', 'visitors', 'employees', ]
        labels = {
            'meeting': 'Numer pokoju',
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
