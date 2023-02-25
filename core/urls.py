from django.urls import path
from core.views import IndexView, LoginView, logout, ClientRegisterView, SupplierRegisterView, ClientUpdateView, \
    SupplierUpdateView, UserUpdateRedirectView, ServiceRegisterView, MyServicesView

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('cadastrar-cliente', ClientRegisterView.as_view(), name='client_register'),
    path('cadastrar-fornecedor', SupplierRegisterView.as_view(), name='supplier_register'),
    path('atualizar-usuario', UserUpdateRedirectView.as_view(), name='user_update'),
    path('atualizar-cliente/<int:pk>', ClientUpdateView.as_view(), name='client_update'),
    path('atualizar-fornecedor/<int:pk>', SupplierUpdateView.as_view(), name='supplier_update'),
    path('cadastrar-servico', ServiceRegisterView.as_view(), name='service_register'),
    path('meus-servicos', MyServicesView.as_view(),  name='my_services'),
]
