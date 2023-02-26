from django.views.generic import FormView
from core.forms import LoginForm
from core.helpers import get_type_user
from django.shortcuts import redirect
from django.contrib import auth


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def get_context_data(self, **kwargs):
        """Método para renderizar página a partir de uma requisição GET"""
        logged_user = get_type_user(self.request.user)
        context = super().get_context_data(**kwargs)
        context['title_page'] = 'login'
        context['type_user'] = logged_user
        return context

    def post(self, request, *args, **kwargs):
        """Método para efetuar a autenticação de usuário"""
        username = request.POST['username']
        password = request.POST['password']

        login_user = auth.authenticate(username=username, password=password)
        if login_user is not None:
            auth.login(request,login_user)
            return redirect('core:index')

        else:
            return redirect('core:login')
