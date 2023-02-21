from django.views.generic import FormView
from core.forms import LoginForm
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = 'login'
        return context

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']

        login_user = auth.authenticate(username=username, password=password)
        if login_user is not None:
            auth.login(request,login_user)
            return redirect('core:index')

        else:
            return redirect('core:login')
