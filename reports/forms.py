from django import forms
from .models import Report
from cities_light.models import Country

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['title', 'category', 'description', 'country', 'state', 'lga', 'street_name']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'category': forms.Select(attrs={'class': 'form-select', 'required': 'required'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'required': 'required'}),
            'country': forms.Select(attrs={'class': 'form-select', 'required': 'required'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'lga': forms.TextInput(attrs={'class': 'form-control'}),
            'street_name': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
        }

    country = forms.ModelChoiceField(queryset=Country.objects.all(), required=True, widget=forms.Select(attrs={'class': 'form-select'}))
