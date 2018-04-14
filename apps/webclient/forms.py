from django import forms

from apps.core.models import Taxi


class TaxiForm(forms.ModelForm):
    class Meta:
        model = Taxi
        exclude = ['usuario']
        widgets = {
            'numero': forms.NumberInput(attrs={'max': 10000, 'placeholder': 'Numero de taxi'})
        }


class TaxiBusquedaForm(forms.ModelForm):
    class Meta:
        model = Taxi
        fields = ['numero']
