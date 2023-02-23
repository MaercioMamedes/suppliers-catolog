from django.views.generic import FormView
from core.forms import SupplierRegisterForm
from django.shortcuts import redirect
from core.helpers import supplier_factor


class SupplierRegisterView(FormView):
    template_name = 'supplierRegister.html'
    form_class = SupplierRegisterForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = 'Cadastro de Fornecedor'
        return context

    def post(self, request, *args, **kwargs):
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