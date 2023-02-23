from django.urls import path
from core.views import IndexView, LoginView, logout, ClientRegisterView, SupplierRegisterView

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('cadastrar-cliente', ClientRegisterView.as_view(), name='client_register'),
    path('cadastrar-fornecedor', SupplierRegisterView.as_view(), name='supplier_register'),
]
