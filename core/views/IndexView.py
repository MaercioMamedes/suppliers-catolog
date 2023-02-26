from django.views.generic.base import TemplateView
from core.helpers import get_type_user
from core.models import Service


class IndexView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        """Método para renderizar página a partir de uma requisição GET"""
        logged_user = get_type_user(self.request.user)  # retorna qual tipo de usuário está logado
        context = super().get_context_data(**kwargs)
        context['title_page'] = 'Nossos serviços'
        context['type_user'] = logged_user
        list_services_published = Service.objects.filter(published=True)
        context['list_services_published'] = list_services_published

        return context

