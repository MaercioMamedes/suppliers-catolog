from django import forms
from core.models import Service, Category


class ServiceRegisterForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['category', 'image', 'title', 'description','price']

    def clean(self):
        print('passou aqui')
        print(self.media)
        print(self.cleaned_data.keys())
        return self.cleaned_data

