from django.views.generic import FormView
from core.forms import ClientRegisterForm
from django.shortcuts import redirect
from core.helpers import client_factor, get_type_user


class ClientRegisterView(FormView):
    template_name = 'clientRegister.html'
    form_class = ClientRegisterForm

    def get_context_data(self, **kwargs):
        """Método para renderizar página a partir de uma requisição GET"""
        logged_user = get_type_user(self.request.user)  # retorna qual tipo de usuário está logado
        context = super().get_context_data(**kwargs)
        context['title_page'] = 'Cadastro de Cliente'
        context['type_user'] = logged_user
        return context

    def post(self, request, *args, **kwargs):
        """Método post para cadastrar no usuário a partir de uma requisição POST"""
        form = ClientRegisterForm(request.POST)

        # método para criar um usuário cliente
        client_factor(
            fullname=form.data.get('fullname'),
            username=form.data.get('username'),
            email=form.data.get('email'),
            cpf=form.data.get('cpf'),
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
