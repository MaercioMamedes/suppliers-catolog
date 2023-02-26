from django.contrib.auth.models import User
from core.models import Client, Supplier


def get_type_user(request_user):

    try:
        user_client = Client.objects.filter(user=request_user).first()
        user_supplier = Supplier.objects.filter(user=request_user).first()

        if user_client is not None:
            return 'client'

        elif user_supplier is not None:
            return 'supplier'

        elif request_user.is_superuser:
            return 'superuser'

    except TypeError:
        return 'anonymous_user'



