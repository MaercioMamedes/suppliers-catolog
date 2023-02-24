from django import forms
from core.helpers import get_federative_unit


class SupplierUpdateForm(forms.Form):
    fantasy_name = forms.CharField(label='Nome da empresa', max_length=200)
    username = forms.CharField(label='usuário', max_length=20)
    email = forms.EmailField(label='email', max_length=100)
    cep = forms.CharField(label='CEP', max_length=9)
    uf = forms.ChoiceField(label='UF', choices=get_federative_unit())
    city = forms.CharField(label='Cidade', max_length=100)
    district = forms.CharField(label='Bairro', max_length=50)
    phone = forms.CharField(label='telefone', max_length=11)
    public_place = forms.CharField(label='Logradouro', max_length=150)
    property_number = forms.CharField(label='Número', max_length=5)
    password = forms.CharField(label='Confirme digitamdo sua senha', max_length=50, widget=forms.PasswordInput)


