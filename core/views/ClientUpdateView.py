from django.views.generic import FormView
from core.forms import ClientUpdateForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from core.models import Client


class ClientUpdateView(FormView):
    template_name = 'ClientUpdate.html'
    form_class = ClientUpdateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = 'Atualização de Cliente'
        return context

    def get_initial(self):
        user = get_object_or_404(User, pk=self.request.user.id)
        user_client = get_object_or_404(Client, user=user)

        return {
            'fullname': user_client.fullname,
            'username': user.username,
            'email': user.email,
            'cep': user_client.cep,
            'uf': user_client.uf,
            'city': user_client.city,
            'district': user_client.district,
            'phone': user_client.phone,
            'public_place':user_client.public_place,
            'property_number': user_client.property_number,
        }

    def post(self, request, *args, **kwargs):
        form = ClientUpdateForm(request.POST)
        user = get_object_or_404(User, pk=kwargs['pk'])
        user_client = get_object_or_404(Client, user=user)

        user.first_name = form.data.get('fullname').split()[0]
        user.last_name = form.data.get('fullname').split()[-1]
        user.username = form.data.get('username')
        user.email = form.data.get('email')

        user.save()

        user_client.fullname = form.data.get('fullname')
        user_client.phone = form.data.get('phone')
        user_client.uf = form.data.get('uf')
        user_client.cep = form.data.get('cep')
        user_client.district = form.data.get('district')
        user_client.public_place = form.data.get('public_place')
        user_client.city = form.data.get('city')
        user.property_number = form.data.get('property_number')

        user_client.save()

        return redirect('core:index')
