from django.shortcuts import redirect
from django.contrib import auth


def logout(request):
    auth.logout(request)
    return redirect('core:index')
