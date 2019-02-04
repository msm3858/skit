from .models import Card, EmployeeCardUsage, VisitorCardUsage
from django import forms


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['name', 'code', 'level_of_privilege']

        labels = {
            'name': 'Opis karty',
            'code': 'Kod karty',
            'level_of_privilege': 'Poziom dostępu',
        }


class EmployeeCardUsageForm(forms.ModelForm):
    class Meta:
        model = EmployeeCardUsage
        fields = ['description', 'card', 'employee']

        labels = {
            'description': 'Opis(cel)',
            'card': 'Karta',
            'employee': 'Pracownik',
        }

        widgets = {
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 5}),
        }


class VisitorCardUsageForm(forms.ModelForm):
    class Meta:
        model = VisitorCardUsage
        fields = ['description', 'card', 'visitor']

        labels = {
            'description': 'Opis(cel)',
            'card': 'Karta',
            'visitor': 'Gość',
        }

        widgets = {
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 5}),
        }
