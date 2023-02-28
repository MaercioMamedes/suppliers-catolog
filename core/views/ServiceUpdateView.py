from django.views.generic import FormView
from core.helpers import get_type_user
from django.shortcuts import get_object_or_404
from core.models import Service
from core.forms import ServiceUpdateForm


class ServiceUpdateView(FormView):
    template_name = 'ServiceUpdate.html'
    form_class = ServiceUpdateForm

    def get_context_data(self, **kwargs):
        """Método para renderizar página a partir de uma requisição GET"""
        logged_user = get_type_user(self.request.user)  # retorna qual tipo de usuário está logado
        context = super().get_context_data(**kwargs)
        context['title_page'] = 'Atualização de Serviço'
        context['type_user'] = logged_user
        return context

    def get_initial(self):
        """Método para buscar os dados do serviço selecionado"""
        service = get_object_or_404(Service, pk=self.kwargs['pk'])

        return {
            'category': service.category,
            'title': service.title,
            'description': service.description,
            'price': service.price,
        }

