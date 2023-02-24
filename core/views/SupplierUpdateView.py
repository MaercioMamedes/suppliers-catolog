from django.views.generic import FormView
from core.forms import SupplierUpdateForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from core.models import Supplier


class SupplierUpdateView(FormView):
    template_name = 'SupplierUpdate.html'
    form_class = SupplierUpdateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = 'Atualização de Fornecedor'
        return context

    def get_initial(self):
        user = get_object_or_404(User, pk=self.request.user.id)
        user_supllier = get_object_or_404(Supplier, user=user)

        return {
            'fantasy_name': user_supllier.fantasy_name,
            'username': user.username,
            'email': user.email,
            'cep': user_supllier.cep,
            'uf': user_supllier.uf,
            'city': user_supllier.city,
            'district': user_supllier.district,
            'phone': user_supllier.phone,
            'public_place':user_supllier.public_place,
            'property_number': user_supllier.property_number,
        }

    def post(self, request, *args, **kwargs):
        form = SupplierUpdateForm(request.POST)
        user = get_object_or_404(User, pk=kwargs['pk'])
        user_supplier = get_object_or_404(Supplier, user=user)

        user.username = form.data.get('username')
        user.email = form.data.get('email')

        user.save()

        user_supplier.fantasy_name = form.data.get('fantasy_name')
        user_supplier.phone = form.data.get('phone')
        user_supplier.uf = form.data.get('uf')
        user_supplier.cep = form.data.get('cep')
        user_supplier.district = form.data.get('district')
        user_supplier.public_place = form.data.get('public_place')
        user_supplier.city = form.data.get('city')
        user_supplier.property_number = form.data.get('property_number')

        user_supplier.save()

        return redirect('core:index')
