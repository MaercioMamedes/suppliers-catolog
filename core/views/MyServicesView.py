from django.views.generic import TemplateView
from core.models import Service, Supplier
from core.helpers import get_type_user


class MyServicesView(TemplateView):
    template_name = 'MyServices.html'

    def get_context_data(self, **kwargs):
        logged_user = get_type_user(self.request.user)
        context = super().get_context_data(**kwargs)

        supplier = Supplier.objects.get(user=self.request.user)
        list_services = Service.objects.filter(supplier=supplier)

        context['title_page'] = 'Index'
        context['type_user'] = logged_user[0]
        context['list_services'] = list_services

        return context
