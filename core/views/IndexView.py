from django.views.generic.base import TemplateView
from core.helpers import get_type_user


class IndexView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        logged_user = get_type_user(self.request.user)
        context = super().get_context_data(**kwargs)
        context['title_page'] = 'Index'
        context['type_user'] = logged_user[0]
        return context

