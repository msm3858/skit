from .models import MeetingDocument, EmployeeDocument
from django import forms




class EmployeeDocumentForm(forms.ModelForm):
    class Meta:
        model = EmployeeDocument
        fields = ['name', 'description', 'kind_of_document', 'file', 'extension', 'employee']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 5}),

        }
        labels = {
            'name': 'Nazwa pliku',
            'description': 'Opis dokumentu',
            'kind_of_document': 'Rodzaj dokumentu',
            'status': 'Status',
            'file': 'Plik',
            'extension': 'Rozszerzenie pliku',
            'employee': 'Pracownik',
        }


class MeetingDocumentForm(forms.ModelForm):
    class Meta:
        model = MeetingDocument
        fields = ['name', 'description', 'kind_of_document', 'file', 'extension', ]
        widgets = {
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 5}),

        }
        labels = {
            'name': 'Nazwa pliku',
            'description': 'Opis dokumentu',
            'kind_of_document': 'Rodzaj dokumentu',
            'status': 'Status',
            'file': 'Plik',
            'extension': 'Rozszerzenie pliku',
        }
