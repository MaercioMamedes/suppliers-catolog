from django.views.generic import FormView
from core.forms import SupplierRegisterForm
from django.shortcuts import redirect
from core.helpers import supplier_factor, get_type_user


class SupplierRegisterView(FormView):
    template_name = 'SupplierRegister.html'
    form_class = SupplierRegisterForm

    def get_context_data(self, **kwargs):
        """Método para renderizar página a partir de uma requisição GET"""
        logged_user = get_type_user(self.request.user)
        context = super().get_context_data(**kwargs)
        context['title_page'] = 'Cadastro de Fornecedor'
        context['type_user'] = logged_user
        return context

    def post(self, request, *args, **kwargs):
        """Método para gravar dados de fornecedores cadastrados a partir de uma requisição POST"""
        form = SupplierRegisterForm(request.POST)
        supplier_factor(
            fantasy_name=form.data.get('fantasy_name'),
            username=form.data.get('username'),
            email=form.data.get('email'),
            cnpj=form.data.get('cnpj'),
            phone=form.data.get('phone'),
            uf=form.data.get('uf'),
            cep=form.data.get('cep'),
            district=form.data.get('district'),
            public_place=form.data.get('public_place'),
            city=form.data.get('city'),
            property_number=form.data.get('property_number'),
            password=form.data.get('password')
        )

        return redirect('core:login')
