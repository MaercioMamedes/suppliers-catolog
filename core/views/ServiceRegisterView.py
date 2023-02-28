from django.views.generic import FormView
from core.forms import ServiceRegisterForm
from core.models import Supplier
from django.shortcuts import redirect, HttpResponse
from core.helpers import get_type_user


class ServiceRegisterView(FormView):
    template_name = 'ServiceRegister.html'
    form_class = ServiceRegisterForm

    def get_context_data(self, **kwargs):
        """Método para renderizar página a partir de uma requisição GET"""
        logged_user = get_type_user(self.request.user)
        context = super().get_context_data(**kwargs)
        context['title_page'] = 'Cadastro de Serviço'
        context['type_user'] = logged_user
        return context

    def post(self, request, *args, **kwargs):
        """Método para gravar dados do serviços cadastrados a partir de uma requisição POST"""
        form = ServiceRegisterForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            new_service = form.save(commit=False)
            user = self.request.user
            user_supplier = Supplier.objects.get(user=user)
            new_service.supplier = user_supplier
            new_service.published = True
            new_service.save()
            return redirect('core:index')

        else:
            print(form.errors)
            return HttpResponse("falha ao salvar formulario")
