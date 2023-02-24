from django.contrib.auth.models import User
from core.models import Client, Supplier


def client_factor(**kwargs):
    user_client = User.objects.create_user(
        first_name=kwargs['fullname'].split()[0],
        last_name=kwargs['fullname'].split()[-1],
        username=kwargs['username'],
        email=kwargs['email'],
    )

    user_client.set_password(kwargs['password'])
    user_client.save()

    Client.objects.create(
        user=user_client,
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
    user_supplier = User.objects.create_user(
        first_name=kwargs['fantasy_name'],
        username=kwargs['username'],
        email=kwargs['email'],
    )

    user_supplier.set_password(kwargs['password'])
    user_supplier.save()

    Supplier.objects.create(
        user=user_supplier,
        phone=kwargs['phone'],
        cnpj=kwargs['cnpj'],
        district=kwargs['district'],
        public_place=kwargs['public_place'],
        uf=kwargs['uf'],
        city=kwargs['city'],
        cep=kwargs['cep'],
        property_number=kwargs['property_number'],
    )

