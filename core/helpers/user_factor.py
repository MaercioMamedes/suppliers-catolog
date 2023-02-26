from django.contrib.auth.models import User
from core.models import Client, Supplier


def client_factor(**kwargs):  # Método para criar usuário cliente
    """Função para criar usuário cliente"""

    user = User.objects.create_user(  # criando usuário genérico
        first_name=kwargs['fullname'].split()[0],
        last_name=kwargs['fullname'].split()[-1],
        username=kwargs['username'],
        email=kwargs['email'],
    )

    user.set_password(kwargs['password'])
    user.save()

    Client.objects.create(
        # Método para criação de usuário cliente que relaciona Um para Um com o usuário genérico criado
        user=user,
        fullname=kwargs['fullname'],
        phone=kwargs['phone'],
        cpf=kwargs['cpf'],
        district=kwargs['district'],
        public_place=kwargs['public_place'],
        uf=kwargs['uf'],
        city=kwargs['city'],
        cep=kwargs['cep'],
        property_number=kwargs['property_number'],
    )


def supplier_factor(**kwargs):
    """Função para criar usuário fornecedor"""

    user = User.objects.create_user(  # criando usuário genérico
        first_name=kwargs['fantasy_name'],
        username=kwargs['username'],
        email=kwargs['email'],
    )

    user.set_password(kwargs['password'])
    user.save()

    Supplier.objects.create(
        # Método para criação de usuário fornecedor que relaciona Um para Um com o usuário genérico criado
        user=user,
        phone=kwargs['phone'],
        cnpj=kwargs['cnpj'],
        district=kwargs['district'],
        public_place=kwargs['public_place'],
        uf=kwargs['uf'],
        city=kwargs['city'],
        cep=kwargs['cep'],
        property_number=kwargs['property_number'],
    )
