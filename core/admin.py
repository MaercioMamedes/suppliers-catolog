from django.contrib import admin
from core.models import Client, Supplier, Service, Message


class ClientAdmin(admin.ModelAdmin):
    list_display = ('user', 'cpf', 'likes')


admin.site.register(Client, ClientAdmin)


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('user', 'cnpj', 'likes')


admin.site.register(Supplier, SupplierAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'category', 'title', 'price', 'published', 'created_in', 'modified_in')


admin.site.register(Service, ServiceAdmin)


class MesageAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'title', 'created_in')


admin.site.register(Message, MesageAdmin)

