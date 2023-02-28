from django import forms
from core.models import Service


class ServiceUpdateForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['category','title', 'description','price']

    def clean(self):
        return self.cleaned_data
