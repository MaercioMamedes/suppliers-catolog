from django.views.generic import View
from django.contrib.auth.models import User
from core.models import Client, Supplier
from django.shortcuts import get_object_or_404, redirect


class UserUpdateRedirectView(View):
    """View para redirecionar para rota de atualização de usuário cliente ou usuário fornecedor"""

    def get(self, *args, **kwargs):
        user = get_object_or_404(User, pk=self.request.user.id)

        try:
            user_client = Client.objects.get(user=user.id)
            return redirect('core:client_update', user_client.id)

        except Client.DoesNotExist:
            user_supplier = get_object_or_404(Supplier, user=user)
            return redirect('core:supplier_update', user_supplier.id)

