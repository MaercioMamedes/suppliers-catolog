from django.contrib import admin
from core.models import Client, Supplier, Service, Message, Category


class ClientAdmin(admin.ModelAdmin):
    list_display = ('user', 'cpf', 'likes', 'city','uf','phone')


admin.site.register(Client, ClientAdmin)


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('user','fantasy_name', 'cnpj', 'likes', 'city','uf','phone')


admin.site.register(Supplier, SupplierAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'category', 'title', 'price', 'published', 'created_in', 'modified_in')


admin.site.register(Service, ServiceAdmin)


class MesageAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'title', 'created_in')


admin.site.register(Message, MesageAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Category, CategoryAdmin)


